
### 盒子模型

> 每个元素都是一个盒子模型, 盒子模型控制着页面这些元素的高度和宽度

1. Border与Content

border是盒子的边框，一般描述边框是否为`实心`, 边框的`厚度`与`颜色`等等，如：

```CSS
border: solid 3px blue;
```

content就是盒子中的主要内容，形象比喻就是一个盒子中装有物品，content就是该物品。

![](https://ws3.sinaimg.cn/large/006tNc79gy1fpovwpmnbej308d083q46.jpg)

2. Padding与margin

Padding指的是内边距,表示`content`到边框`border`的距离。

![](https://ws1.sinaimg.cn/large/006tNc79gy1fpovws8j90j30a306jtab.jpg)

Margin指的是外边距，表示`content`之间，或者`content`与`上层元素`之间的距离。

![](https://ws1.sinaimg.cn/large/006tNc79gy1fpovwuvxfij30b205s0ts.jpg)



简单理解：

**padding为内推，margin为外攘。**padding通过挤压的方式调整`内部元素`到`内部中心`的位置，margin通过外攘的方式调整`该元素`距离`外部元素`的大小。



3. 重要属性box-sizing

Box-sizing是css3新属性，为了改变ie浏览器的盒模型遗留的width bug。

**盒模型的width bug**：

盒子模型包含content、padding、border几部分内容，默认情况下盒子模型的尺寸（width和height）指的是内容框content的尺寸，也就是内边距padding与border没有计算在内，这与生活中的思维方式显然相悖。

如果将盒子模型想象成一个快递包裹，那里面的货物就是内容框，货物外面包的泡沫包装就是内部填充padding，快递纸盒的厚度就是边框border，我们描述尺寸的时候一般指的是整个包裹的尺寸，而并非单指货物的尺寸，显然这与CSS盒子模型对尺寸的定义相违背了。

为解决这个理解上的冲突，在css3中引入了box-sizing定义，主要的两个属性为：`content-box | border-box`

当属性为content-box时，参照生活中思维方式理解，盒子的宽度width会比css文件中定义的width大，大的数值为padding与border之和:

> 盒子的`真实width = width + padding +border`; 

当属性为border-box时，盒子的宽度即为css文件中定义的width值:

> 盒子的`真实width = 原width`;

在涉及到width、height时尽量使用`border-box`来定义，避免一些不必要的麻烦。

如本次实验中的示例：

![](https://ws3.sinaimg.cn/large/006tNc79gy1fpoy9e6ja1j30js0fp76f.jpg)

![](https://ws3.sinaimg.cn/large/006tNc79gy1fpoycfzu2oj30vy0d3mzf.jpg)

在第block里，css文件定义其宽度为64，但是实际上width为：4px + 14px + 64px + 14px + 4px = 100px

```css
.block1 {
    border: solid 4px blue;
    background: tomato;
    margin-bottom: 20px;
    padding: 20px 14px 20px 14px;
    /* box-sizing: border-box;  */
    width: 64px;
    height: 64px;
}
```

而在block2和block3中定义了`box-sizing: border-box`;则block大小为实际定义大小。

```css
.block2 {
    border: solid 4px red;
    background: green;
    margin-bottom: 20px;
    padding: 20px 14px 20px 14px;
    box-sizing: border-box; 
    width: 64px;
    height: 64px;
}

.block3 {
    border: solid 4px black;
    background: blueviolet;
    margin-bottom: 20px;
    padding: 20px 14px 20px 14px;
    box-sizing: border-box; 
    width: 64px;
    height: 64px;
}
```

