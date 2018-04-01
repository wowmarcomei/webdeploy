### 展示背景图

有时候希望背景图尽可能多的展示在div中的时候，需要使用`background-position`来对其位移。如：

```css
.ui.vertical.segment.masthead {
    height: 300px;
    background: url('../images/star_banner.jpg');
    background-size: cover;
    background-position: 100% 80%;
}
```

其中`x% y%`表示水平位置和垂直位置，左上角为0%, 0%,右下角为100%，100%。默认值为左上角0%，0%。一定要注意:

> `background-position: x% y%`中间没有逗号。—这是自己一开始犯的错误。



### 下拉菜单

在semantic中可以使用`dropdown`配合`item`使用可以获取到下拉菜单。使用`simple`修饰该`item`可以得到类似的`hover`效果。

![](https://github.com/wowmarcomei/workstation/blob/master/python_web/level1/ex8_custom_home_page/ex8.png)