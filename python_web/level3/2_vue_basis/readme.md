# Vue.js初使用

### 1.在模板中引用vue.js

```html
<script type="text/javascript" src="js/vue1.js"></script>
```

### 2.直接在模板中创建实例

- 设置body的id，如`app`

```html
<body id="app"></body>
```

- 添加Vue.js实体管理body

```html
<script>
    // 创建Vue实例来进行管理页面
    var vm = new Vue({
        // 使用el(element)来定义管理区域，一般这个el选择这个页面的body
        // 定义完了el后，Vue就可以管理整个body
        el: "#app",
        // 使用data管理数据，配合django使用时，一般是从django中取出数据，相当于在django
        // 中从view往template中输送数据的context字典
        // 类似于django中的：content['article']=article
        data: {
			article:{
                        title: "This is the title",
                        content:"Hi, there"
            },
        }
    })
</script>
```

> - 使用`el`来定义管理区域，一般这个`el`选择这个页面的`body`
> - 使用`data`加载数据

### 3.使用`v-for`指令来进行循环处理

`<div v-for="comment in comments"></div> `

- 在Vue对象中的data中添加列表数据`comments`

```vue
<script>
    // 创建Vue实例来进行管理页面，类似于django中的template管理模板一样
    var vm = new Vue({
        // 使用el(element)来定义管理区域，一般这个el选择这个页面的body
        // 定义完了el后，Vue就可以管理整个body
        el: "#app",
        // 使用data管理数据，配合django使用时，一般是从django中取出数据，相当于在django
        // 中从view往template中输送数据的context字典
        // 类似于django中的：content['article']=article
        data: {
            // 定义一个article对象
            article:{
                title: "This is the title",
                content:"Hi, there"
            },
            // 定义一个列表，列表中定义了多个对象
            comments:[
                {name:"John Doe",said:"Well done!"},
                {name:"Marco",said:"Greate!"},
                {name:"Tony",said:"Good Job!"},
                {name:"John Snow",said:"Very Nice!"},
            ]
        }
    })
</script>
```

- 在模板html中添加`v-for`循环，需要注意的是，要在元素的上一级元素中添加`v-for`循环指令

```html
        <!-- Comments&Form's here -->
        <div class="ui segment container" style="width:700px;">
            <h3 class="ui header" style="font-family:'Oswald', sans-serif;">Comments</h3>
            <div v-for="comment in comments" class="ui comments">
                <div class="comment">
                    <div class="avatar">
                        <img src="images/matt.jpg" alt="" />
                    </div>
                    <div class="content">
                        <a href="#" class="author">{{ }}</a>

                        <p class="text" style="font-family: 'Raleway', sans-serif;">
                            {{ }}
                        </p>
                    </div>
                </div>

            </div>
            <div class="ui divider"></div>

            <form class="ui form" action="index.html" method="post">
                <input type="text">
            </form>
        </div>
```

![](http://ww1.sinaimg.cn/large/67c0b572ly1fqqx8uir24j20hp0fi3yu.jpg)

### 4.使用`v-model`指令存储临时变量

上面的例子是在Vue对象中通过获取data中的对象来获取值，而Vue可以通过`v-model`指令获取到页面输入值，存入临时变量中。

- 在模板html中的`input`标签中加入`v-model`指令

```html
<input v-model="message" type="text">
```

- 在模板中渲染`input`输入的数据

```html
<h3 class="ui header">{{ message }}</h3>
```

即模板中关于评论部分的全部代码为：

```html
<!-- Comments&Form's here -->
<div class="ui segment container" style="width:700px;">
    <h3 class="ui header" style="font-family:'Oswald', sans-serif;">Comments</h3>
    <div v-for="comment in comments" class="ui comments">
        <div class="comment">
            <div class="avatar">
                <img src="images/matt.jpg" alt="" />
            </div>
            <div class="content">
                <a href="#" class="author">{{comment.name}}</a>

                <p class="text" style="font-family: 'Raleway', sans-serif;">
                    {{comment.said}}
                </p>
            </div>
        </div>

    </div>
    <div class="ui divider"></div>
    <h3 class="ui header">{{ message }}</h3>
    <form class="ui form" action="index.html" method="post">
        <input v-model="message" type="text">
    </form>
</div>
```

![](https://ws3.sinaimg.cn/large/006tNc79gy1fqqxpj01bnj30h20fut9k.jpg)

- 及时显示字数统计

```html
<h3 class="ui header">还可以输入{{ 200-message.length }}字</h3>
```

![](https://ws4.sinaimg.cn/large/006tNc79ly1fqqy0y4kp1j30hg0g8wfh.jpg)