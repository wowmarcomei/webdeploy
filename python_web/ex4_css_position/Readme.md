### Position定位

CSS中主要通过relative与absolute属性来进行定位，要定位`块/盒子`则需要确定两点：

> 1. 定位系统参照坐标系
> 2. 定位系统的坐标点

CSS中定位任何`块/盒子`时，均已该`块/盒子`的左上角的点为坐标点，移动该点时就会移动整个`块/盒子`。

- relative参考坐标系：自己**之前本应该在的位置**为参考系，**且偏移后该元素本来在的位置依然保持不变**。
- absolute参考坐标系：以自己的父级元素为参考系，**且偏移后该元素原来的位置会漂浮出来**，就是**说不再占用以前的位置了**，相对与原位置跳出一层了; 同时，使用absolute有一个前提条件**是该元素的父级元素的类必须使用了`absolute`或者`relative`修饰**。

移动`块/盒子`时，使用position字段且指定属性来进行。如下示例，

1.html文件指明元素

```html
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <title>Page Title</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" type="text/css" media="screen" href="./main.css" />
</head>
<body>
    <div class="flower">
        <div class="point">

        </div>
    </div>

    <div class="block1"></div>

    <div class="block2"></div>

    <div class="block3"></div>

</body>
</html>
```

2.css修饰元素

```css
.block1 {
    box-sizing: border-box; 
    width: 64px;
    height: 64px;
    background: url(images/grass.png);
    background-size: contain;
}

.block2 {
    box-sizing: border-box; 
    width: 128px;
    height: 64px;
    background: url(images/grass.png);
    background-size: contain;
}

.block3 {
    box-sizing: border-box; 
    width: 196px;
    height: 64px;
    background: url(images/grass.png);
    background-size: contain;
}

.flower{
    box-sizing: border-box; 
    width: 64px;
    height: 64px;
    background: url(images/rose.png);
    background-size: contain;
    position: relative; 
    left: 64px; /*自己原本在的位置相对新位置，向左偏移了64px */
    top:64px; /*自己原本在的位置相对新位置，向上偏移了64px */
    /* 由于是相对偏移，所以自己本来的div所在的位置还保留 */
}

.point{
    background: orange;
    width: 8px;
    height: 8px;
}
```

在html中指定了flower这个div本来在三个block之上，这就是flower这个div**原本在的位置**，在css中通过指定`position`修改其属性为`relative`，表示将使用flower这个类修饰的div将会被相对偏移，`left:64px;`，`top: 64px;`表示**原来的位置**相对**新位置**向左和向上偏移64px，即**新位置**向右和向下偏移64px；

![](https://ws3.sinaimg.cn/large/006tNc79ly1fppc1bk80mj307i08ljs4.jpg)

举例说明absolute定位如下：

1.html中有一个div使用css类bg来修饰，里面有5个div，其中`第一个div`使用类flower修饰，该类指明背景为一朵红花(里面嵌套一个类为point的div，背景为黄色)，`第二个div`使用类block1修饰，`第三个div`使用yellow-flower修饰，`第四个div`使用block2修饰，`第五个div`使用block3修饰。

```html
<body>

    <div class="bg">
        <div class="flower">
            <div class="point">

            </div>
        </div>

        <div class="block1"></div>

        <div class="yellow-flower">
            <div class="point"></div>
        </div>

        <div class="block2"></div>

        <div class="block3"></div>
    </div>


</body>
```

2.CSS的定义如下

```css
.block1 {
    box-sizing: border-box; 
    width: 64px;
    height: 64px;
    background: url(images/grass.png);
    background-size: contain;
}

.block2 {
    box-sizing: border-box; 
    width: 128px;
    height: 64px;
    background: url(images/grass.png);
    background-size: contain;
}

.block3 {
    box-sizing: border-box; 
    width: 196px;
    height: 64px;
    background: url(images/grass.png);
    background-size: contain;
}

.flower{
    box-sizing: border-box; 
    width: 64px;
    height: 64px;
    background: url(images/rose.png);
    background-size: contain;
    position: relative; 
    left: 64px; /* 自己原本在的位置相对新位置，向左偏移了64px */
    top:64px;/* 自己原本在的位置相对新位置，向上偏移了64px */
    /* 由于是相对偏移，所以自己本来的div所在的位置还保留 */
    
}

.yellow-flower{
    box-sizing: border-box; 
    width: 64px;
    height: 64px;
    background: url(images/flower.png);
    background-size: contain;
    position: absolute; 
    left: 128px;
}

.point{
    background: orange;
    width: 8px;
    height: 8px;
}

.bg{
    background: midnightblue;
    width: 320px;
    height: 256px;
}
```

其中yellow-flower使用使用relative定位时，即使向右偏移了128px，原有位置依然保持，如果换成absolute以后偏移128px后原先位置向上一层浮起，不再占有；但是由于yellow-flower修饰的div的父级元素div在css中使用了bg来修饰，bg必须使用`relative`或者`absolute`修饰才能**完全正确地偏移**，否则以yellow-flower的父级的父级(的父级的父级...)元素的CSS样式来为坐标系，直到有父级元素的CSS样式有`relative`或者`absolute`修饰。

![](https://ws1.sinaimg.cn/large/006tNc79gy1fppewcqzwmj30nk0d7784.jpg)

![](https://ws3.sinaimg.cn/large/006tNc79gy1fppewg9a8oj30no0cwq6w.jpg)

![](https://ws1.sinaimg.cn/large/006tNc79gy1fppewjuwb9j30nf0hfwkn.jpg)



### 元素居中处理

内层元素处于外层元素的50%的绝对位置即可完成居中处理，此时的居中是以元素的左上角为坐标系，所以需要改定位点为元素中心点。即：

1. 设置需要偏移的元素的CSS修饰样式的`position`为`absolute`属性。
2. 设置该元素对外层元素的偏移位置为`left: 50%;`与`top: 50%;` 。
3. 设置偏移坐标系的原点从左上角改为中心处：`transform: translate(-50%,-50%);`

接着上叙示例就是：

html文件：

```html
<body>

    <div class="bg">
        <div class="flower">
            <div class="point">

            </div>
        </div>

        <div class="block1"></div>

        <div class="yellow-flower">
            <div class="point"></div>
        </div>

        <div class="block2"></div>

        <div class="block3"></div>
    </div>


</body>
```

css文件：

因为要修改的是body中div的位置，该元素使用CSS样式bg类修饰，所以需要对bg类进行修改如下。

```css
.block1 {
    box-sizing: border-box; 
    width: 64px;
    height: 64px;
    background: url(images/grass.png);
    background-size: contain;
}

.block2 {
    box-sizing: border-box; 
    width: 128px;
    height: 64px;
    background: url(images/grass.png);
    background-size: contain;
}

.block3 {
    box-sizing: border-box; 
    width: 196px;
    height: 64px;
    background: url(images/grass.png);
    background-size: contain;
}

.flower{
    box-sizing: border-box; 
    width: 64px;
    height: 64px;
    background: url(images/rose.png);
    background-size: contain;
    position: relative; 
    left: 64px; /* 自己原本在的位置相对新位置，向左偏移了64px */
    top:64px;/* 自己原本在的位置相对新位置，向上偏移了64px */
    /* 由于是相对偏移，所以自己本来的div所在的位置还保留 */
    
}

.yellow-flower{
    box-sizing: border-box; 
    width: 64px;
    height: 64px;
    background: url(images/flower.png);
    background-size: contain;
    position: absolute; 
    left: 128px;
}

.point{
    background: orange;
    width: 8px;
    height: 8px;
}

.bg{
    border: solid 8px rgb(212, 143, 15);
    background: blue;
    width: 320px;
    height: 256px;
    position: absolute;
    left: 50%;
    top: 50%;
    transform: translate(-50%,-50%);
}

body{
    margin: 0;
    background: url('images/brick.jpg');
    background-size: 150px 150px;
}
```

最终即可达到如下效果图：

![](https://ws2.sinaimg.cn/large/006tNc79gy1fppfru43nwj30wn0h3aef.jpg)