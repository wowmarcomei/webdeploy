## Vue.js实现弹窗功能

#### 1.在Vue的data中添加对象变量modal

`modal:{ show:true,}`

定义一个BOOL变量判断其状态

#### 2.在vue中添加函数`modalSwitch`切换BOOL值状态

`    methods:{ modalSwitch:function() { this.modal.show = !this.modal.show} }`

> ready函数表示的是一旦加载了vm管理区时候，就开始执行的函数，一般以此作为初始化函数。

完整的vm定义如下：

```javascript
<script>
    var vm = new Vue({
        el:"#app",
        // context
        data:{
            // context["article"] = article
            article:{
                title:"This is a title",
                content:"Hi there!",
                fontSize:14
            },
            comments:[
                {name:"John Doe1",said:"Great!",show:true},
                {name:"John Doe2",said:"Good!",show:true},
                {name:"John Doe3",said:"Nice!",show:true},
                {name:"John Doe4",said:"Well done!",show:true},
            ],
            modal:{
                show:true,
            }
        },
        methods:{
            modalSwitch:function()  {
                this.modal.show = !this.modal.show
            }
        },
        ready:function(){
            this.modalSwitch()
        }
    })
</script>
```

#### 3.定义一个弹窗

```html
<div class="ui dimmer active fadeIn" v-if="!modal.show" v-on:click="modalSwitch">
    <div class="ui modal active">
        <h3 class="ui header">提醒：不要再这样做了，知道了吗？</h3>
    </div>
</div>
```

> 其中class `fadeIn` 来自于animate样式，`v-if`为Vue判断语句，`v-on:click`为Vue点击事件。表明如果该值为`false`的时候将显示弹窗，单击时执行`modalSwitch`函数。

#### 4.定义一个按钮

```html
 <button class="ui inverted blue button" type="button" v-on:click="modalSwitch">
     Subscribe me
 </button>
```

![](http://ww1.sinaimg.cn/large/67c0b572gy1fqufwc4xpnj20h70h9aaf.jpg)

![](http://ww1.sinaimg.cn/large/67c0b572gy1fqufwie0guj20h70h9q3t.jpg)

