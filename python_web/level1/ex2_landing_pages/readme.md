![](https://ws1.sinaimg.cn/large/006tNc79gy1fpmvyizzozj311y0x8kiw.jpg)

### 1. 网页设计一般结构
- 菜单
- 图片展示窗
- 内容区
- Footer区

### 2. 菜单设计
semantic中menu一般搭配item使用，如下：

```html
<div class="ui fixed inverted menu">
        <a href="#" class="item">Home</a>
        <a href="#" class="item">About</a>
        <a href="#" class="item">Other</a>
</div>
```

> 通过设置menu其属性为`fixed` `inverted` 可以去掉下面div的黑边框的视觉效果

### 3. 图片展示区
semantic中使用ui segment 与ui image搭配使用加载图片。

```html
<div class="ui segment vertical basic">
        <div class="ui image">
            <img src="./images/banner.jpg" alt="">
        </div>
</div>
```

> 使用`basic`修饰segment可以将其圆角化，这样segment外边的线条就会消失


### 4. 内容栏
一般使用栅格系统设计内容栏，栅格最大为16格，超过后会自动换行。
 Semantic中栅格使用方法：在div中嵌套进如下代码,即使用grid，里面再套入column.注一个栅格最大宽度为16.
 
 
```html
<div class="ui grid">
    <div class="ten wide column">
        <!---->
    </div>

    <div class="six wide column">
        <!---->
    </div>
</div>
```

### 5. 底部栏
与内容栏一样，一般使用栅格设计，除此之外搭配text menu使用。


```html
<div class="ui vertical inverted text menu">
                    <h3 class="header">Company</h3>
                    <div class="item">
                        Add: CN
                    </div>
                    <div class="item">
                        Tel: 010-123456
                    </div>
                    <div class="item">
                        Fax: 010-123456
                    </div>
                    <div class="item">
                        Tel: 010-123456
                    </div>
                    <div class="item">
                        Fax: 010-123456
                    </div>
</div>
```
