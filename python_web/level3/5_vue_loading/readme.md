#Computed属性基本知识

Computed属性与方法Methods类似，但是

## [计算属性](https://cn.vuejs.org/v2/guide/computed.html#%E8%AE%A1%E7%AE%97%E5%B1%9E%E6%80%A7)

模板内的表达式非常便利，但是设计它们的初衷是用于简单运算的。在模板中放入太多的逻辑会让模板过重且难以维护。例如：

```
<div id="example">
  {{ message.split('').reverse().join('') }}
</div>
```

在这个地方，模板不再是简单的声明式逻辑。你必须看一段时间才能意识到，这里是想要显示变量 `message` 的翻转字符串。当你想要在模板中多次引用此处的翻转字符串时，就会更加难以处理。

所以，对于任何复杂逻辑，你都应当使用**计算属性**。

### [基础例子](https://cn.vuejs.org/v2/guide/computed.html#%E5%9F%BA%E7%A1%80%E4%BE%8B%E5%AD%90)

```html
<div id="example">
  <p>Original message: "{{ message }}"</p>
  <p>Computed reversed message: "{{ reversedMessage }}"</p>
</div>
```

```js
var vm = new Vue({
  el: '#example',
  data: {
    message: 'Hello'
  },
  computed: {
    // 计算属性的 getter
    reversedMessage: function () {
      // this 指向 vm 实例
      return this.message.split('').reverse().join('')
    }
  }
})
```

结果：

Original message: "Hello"

Computed reversed message: "olleH"

这里我们声明了一个计算属性 `reversedMessage`。我们提供的函数将用作属性 `vm.reversedMessage` 的 getter 函数：

```
console.log(vm.reversedMessage) // => 'olleH'
vm.message = 'Goodbye'
console.log(vm.reversedMessage) // => 'eybdooG'
```

可以打开浏览器的控制台，自行修改例子中的 vm。`vm.reversedMessage` 的值始终取决于 `vm.message` 的值。

其实可以像绑定普通属性一样在模板中绑定计算属性。Vue 知道 `vm.reversedMessage` 依赖于 `vm.message`，因此当 `vm.message` 发生改变时，所有依赖 `vm.reversedMessage` 的绑定也会更新。而且最妙的是我们已经以声明的方式创建了这种依赖关系：计算属性的 getter 函数是没有副作用 (side effect) 的，这使它更易于测试和理解。

### [计算属性缓存 vs 方法](https://cn.vuejs.org/v2/guide/computed.html#%E8%AE%A1%E7%AE%97%E5%B1%9E%E6%80%A7%E7%BC%93%E5%AD%98-vs-%E6%96%B9%E6%B3%95)

你可能已经注意到我们可以通过在表达式中调用方法来达到同样的效果：

```html
<p>Reversed message: "{{ reversedMessage() }}"</p>
```

```js
// 在组件中
methods: {
  reversedMessage: function () {
    return this.message.split('').reverse().join('')
  }
}
```

我们可以将同一函数定义为一个方法而不是一个计算属性。两种方式的最终结果确实是完全相同的。然而，不同的是**计算属性是基于它们的依赖进行缓存的**。计算属性只有在它的相关依赖发生改变时才会重新求值。这就意味着只要 `message` 还没有发生改变，多次访问 `reversedMessage` 计算属性会立即返回之前的计算结果，而不必再次执行函数。

这也同样意味着下面的计算属性将不再更新，因为 `Date.now()` 不是响应式依赖：

```js
computed: {
  now: function () {
    return Date.now()
  }
}
```

相比之下，每当触发重新渲染时，调用方法将**总会**再次执行函数。

我们为什么需要缓存？假设我们有一个性能开销比较大的的计算属性 **A**，它需要遍历一个巨大的数组并做大量的计算。然后我们可能有其他的计算属性依赖于 **A** 。如果没有缓存，我们将不可避免的多次执行 **A** 的 getter！如果你不希望有缓存，请用方法来替代。**因为使用计算属性要比方法性能更好**。

### [计算属性的 setter](https://cn.vuejs.org/v2/guide/computed.html#%E8%AE%A1%E7%AE%97%E5%B1%9E%E6%80%A7%E7%9A%84-setter)

计算属性默认只有 getter ，不过在需要时你也可以提供一个 setter ：

```js
// ...
computed: {
  fullName: {
    // getter
    get: function () {
      return this.firstName + ' ' + this.lastName
    },
    // setter
    set: function (newValue) {
      var names = newValue.split(' ')
      this.firstName = names[0]
      this.lastName = names[names.length - 1]
    }
  }
}
// ...
```

现在再运行 `vm.fullName = 'John Doe'` 时，setter 会被调用，`vm.firstName` 和 `vm.lastName` 也会相应地被更新。



## 实战computed属性

### 基本computed使用

`computed`与`methods`同级别使用，不同于`methods`的是`computed`需要返回值。

```javascript
<script>
    var vm = new Vue({
        el:"#app",
        // context
        data:{

            modal:{
                show:true,
            },
            // context["article"] = article
            article:{
                title:"This is a title",
                content:"Hi there!",
                fontSize:18
            },
            comments:[
                // {name:"John Doe",said:"Great!",show:true},
                // {name:"John Doe",said:"Great!",show:true},
                // {name:"John Doe",said:"Great!",show:true},
                // {name:"John Doe",said:"Great!",show:true},
            ]
        },
        methods:{
            modalSwitch:function () {
                this.modal.show = !this.modal.show

            },
            getData:function () {
                var self = this;
                reqwest({
                    url:"https://swapi.co/api/people/?format=json",
                    type:"json",
                    method:"get",
                    success:function (resp) {
                        self.comments = resp.results;
                    }
                })
            }
        },
        computed:{
            loadingOrNot: function(){
                if (this.comments.length == 0){
                    return ' loading'
                }else{
                    return ''
                }
            },
        },
        ready:function () {
            this.getData()
        }
    })
</script>
```

在模板html中加入属性`loadingOrNot`的字段，使用大括号即可引用，当评论没有加载完，其长度为0，则`{{ loadingOrNot }}`即为` loading`，评论加载完成时其长度非0则`{{ loadingOrNot }}`为空，将其加入对`div`的CSS修饰。

```html
        <!-- Comments&Form's here -->
        <div class="ui segment {{loadingOrNot}} container" style="width:700px;">
            <h3 class="ui header" style="font-family:'Oswald', sans-serif;">Comments</h3>
            <div v-for="comment in comments" class="ui comments">
                <div class="comment" >
                    <div class="avatar">
                        <img src="images/matt.jpg" alt="" />
                    </div>
                    <div class="content">
                        <a href="#" class="author">{{ comment.name }}</a>

                        <p class="text" style="font-family: 'Raleway', sans-serif;">
                            My height is {{ comment.height }} cm
                        </p>
                        
                    </div>
                </div>
                
            </div>
            <div class="ui divider"></div>
            <h3 class="ui header"> 你还可以输入 {{ 200 - message.length }} 字 </h3>

            <form class="ui form" action="index.html" method="post">
                <input v-model="message" type="text">
            </form>
        </div>
```

![](https://ws2.sinaimg.cn/large/006tKfTcgy1fr0fkzogimj30hf0dq3yu.jpg)

![](https://ws4.sinaimg.cn/large/006tKfTcgy1fr0fl26gn7j30hi0hwq3a.jpg)

### 利用Computed属性对页面数据二次加工

> 类似于Django的过滤器，不对原始数据进行任何修改，仅仅对数据进行过滤选择

参考[Mozilla Developer](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/Array/filter)中的过滤器实现方法：

#####  例子：筛选排除掉所有的小值

下例使用 `filter` 创建了一个新数组，该数组的元素由原数组中值大于 10 的元素组成。

```
function isBigEnough(element) {
  return element >= 10;
}
var filtered = [12, 5, 8, 130, 44].filter(isBigEnough);
// filtered is [12, 130, 44]
```

应用到本次实验中：

```javascript
computed:{
    loadingOrNot: function(){
        if (this.comments.length == 0){
            return ' loading'
        }else{
            return ''
        }
    },
    // 对页面数据进行二次加工：过滤掉身高小于100cm的用户
    filteredList: function () {
        // 参考 developer.mozilla中的过滤器
        function useRuler(people) {
            return people.height > 160
        }
        // 回调函数，回调的参数为this.comments
        var newList = this.comments.filter(useRuler)
        return newList
    },
},
```

修改html模板中变量为`filteredList`

```html
<div v-for="comment in filteredList" class="ui comments">
<!-- <div v-for="comment in comments" class="ui comments"> -->
    <div class="comment" >
        <div class="avatar">
            <img src="images/matt.jpg" alt="" />
        </div>
        <div class="content">
            <a href="#" class="author">{{ comment.name }}</a>

            <p class="text" style="font-family: 'Raleway', sans-serif;">
                My height is {{ comment.height }} cm
            </p>
            
        </div>
    </div>

</div>
```

![](https://ws2.sinaimg.cn/large/006tKfTcgy1fr0gefqc2uj30hi0h63ys.jpg)