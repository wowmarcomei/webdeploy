### Vue.js核心功能：数据驱动界面

#### 1. v-on:click使用

`v-on:click`点击某个地方，让数据发生变动，进而直接显示在界面上。

eg: 定义`p`标签字体大小取值自Vue对象中定义的大小`fontSize`,添加按钮`button`每次点击的时候`p`标签的大小会加5。

1. 设置`Vue`对象的作用域与数据。

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
                {name:"John Doe",said:"Great!"},
                {name:"John Doe",said:"Great!"},
                {name:"John Doe",said:"Great!"},
                {name:"John Doe",said:"Great!"},
            ]
        }
    })
</script>
```

其中作用域为`body`,管理的是`body`下面的所有元素，数据`data`中定义了对象`article`与列表`comments`,`comments`里有多个对象，在`article`中定义了字体大小初始值为`14`。

2. 在`body`下面设置内联样式，指定`p`大小

> 之所以要在`body`下面是因为定义的`Vue`对象的作用范围为`body`.

```html
   <body id="app">

        <style type="text/css">
            ...

            p {
                font-family: 'Raleway', sans-serif;
                font-size: {{article.fontSize}}px;
            }

           ....

        </style>
       ...
</body>
```

3. 添加一个按钮标签`button`,关联`v-on:click`事件

格式为：`v-on:click="函数名/直接运算"`

```html
<div class="ui  segment padded container" >
    <button v-on:click="article.fontSize+=5" class="ui top left attached label" type="button">
        +
    </button>
    <h1 class="ui header">
        {{ article.title }} 
        {{ article.fontSize }}

    </h1>
    <p>
        {{ article.content }}
    </p>
</div>
```

![](https://ws1.sinaimg.cn/large/006tNc79gy1fqtk3gd30bj30h60gyq33.jpg)

![](https://ws3.sinaimg.cn/large/006tNc79gy1fqtk3jcxynj30hc0gx0sy.jpg)

#### 2. v-if使用

使用格式：

```html
<div v-if="condition">
    ...
</div>
<div v-else>
    ...
</div>
```

eg：屏蔽掉不需要的评论。

思路：在Vue数据中的评论变量添加一个bool值，指示是否显示该评论。当点击某个按钮或者点击时，改变该评论是否显示。

```javascript
<script>
    var vm = new Vue({
        el:"#app",
        // context
        data:{
            ...
            comments:[
                {name:"John Doe1",said:"Great!",show:true},
                {name:"John Doe2",said:"Good!",show:true},
                {name:"John Doe3",said:"Nice!",show:true},
                {name:"John Doe4",said:"Well done!",show:true},
            ]
        }
    })
</script>
```

在`div`中添加`v-if`与`v-else`判断语句，且在下面添加`a`标签，设置点击时该值取反，所以当点击`隐藏`时该评论不可见，执行后续的`v-else`语句。

```html
<div v-for="comment in comments" class="ui comments">
    <!-- 如果评论show为true则执行如下语句 -->
    <div class="comment"  v-if="comment.show">
        ...
        <div class="content">
           ...
            <div class="actions">
                <a v-on:click="comment.show = !comment.show">隐藏</a>
            </div>
        </div>
    </div>
    <!-- 如果评论show为false则执行如下语句 -->
    <div class="comment"  v-else>
        Oops!!!
    </div>    
    
</div>
```

![](https://ws3.sinaimg.cn/large/006tNc79gy1fqtlai0y9fj30h60gj3yn.jpg)