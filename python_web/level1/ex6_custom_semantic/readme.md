### 定制Semantic CSS

指的是先引用原生semantic修饰元素，然后通过新定义一个CSS文件，在里面订制一些基本样式，比如背景图，长宽，居中设置等等。

1. 创建并引入新的订制css文件
```css
<link rel="stylesheet" href="custom.css" media="screen" title="no title">
```

2. 添加元素修饰样式

> 定制Semantic css，只需在原有的类后加上自己的类，如下除了`masthead`外均为semantic自身样式，加上masthead之后，就可以在里面定制长宽`height`与`weight`，背景`backgroud`，`padding`等等 

```css
.ui.segment.vertical.basic.masthead {
   height: 700px;
   background: url(./images/banner.png);
   background-size: cover;
   padding-left: 40px;
   padding-right: 40px;
}
```



![](https://ws2.sinaimg.cn/large/006tKfTcgy1fpr6zcmpa4j311y1ml4qq.jpg)
