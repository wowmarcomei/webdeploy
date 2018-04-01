### 引用Google字体

1. 首先需要在html中引用字体

```html
 <link href="https://fonts.googleapis.com/css?family=Oswald|Raleway" rel="stylesheet">
```

2. 在css文件中或者在style中使用字体

```css
.paragraph-content {
    font-family: 'Raleway', sans-serif;
    font-size:18px;
}
```



### 在Semantic中使用comments作为评论

参考官网：[Semantic Comments](https://semantic-ui.com/views/comment.html)

如下示例：

```css
<div class="ui comments">
            <div class="comment">
                <!-- 图像部分 -->
                <div class="avatar">
                    <img src="http://semantic-ui.com/images/avatar/small/matt.jpg" alt="" />
                </div>
                <!-- 内容部分 -->
                <div class="content">
                    <a class="author">Elliot Fu</a>
                    <div class="metadata">
                        <div class="date">2 days ago</div>
                    </div>
                    <p class="text" style="font-family: 'Raleway', sans-serif;">
                        Great article !
                    </p>
                </div>
            </div>
        </div>
```

达到的效果:

![](https://ws2.sinaimg.cn/large/006tKfTcly1fpx04rpm24j30g901nmwy.jpg)

注意一点：

> `div`，`p`，`header`这些全部是块元素，也就是说默认他们是占据一行的，可以自动换行。

### 表单的写法

```css
 <form class="ui form" action="" method="post">
            <div class="field">
                <label>Name</label>
                <input type="text">
            </div>
            <div class="field">
                <label>Content</label>
                <textarea name="" id="" cols="30" rows="10"></textarea>
            </div>
            <button class="ui blue button" type="button">Submit</button>
        </form>
```

