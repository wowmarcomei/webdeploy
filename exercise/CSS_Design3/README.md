# CSS 设计指南学习总结

> 本目录里的代码来源于CSS设计指南-第三版，此处为学习该书的学习总结

## 1.DOM模型
DOM即 document object module，翻译过来就是文档对象模型，DOM是从浏览器的视角来观察页面中的元素及元素的属性，由此得出这个元素的家族树。简而言之，通过DOM可以确定元素之间的相互关系。

## 2.CSS工作原理

### 2.1 上下文选择符
> 使用空格隔开选择标签, 只有后面的后代才会被选中应用后面的样式,也叫做:"后代组合式选择符"

```html
        article h1 {color: black;font-size: medium}
        article p {color: black; font-size: large}

        /*本样式指明只有选择了aside,p标签之后的em标签才会使用下面的样式*/
        aside p em {color: firebrick}

        /*本样式指明只有p标签的后代em才会应用下面的样式,不用关注p标签的父标签*/
        p em {color: firebrick}
```
       
### 2.2 ID和类选择符
> ID选择符使用#, 类选择符选择.

```html
        /*!!!重点 1: 标签带类选择器,使用一个点号.*/
        p.specialtext {color: red;}

        /*扩展标签带类选择器: 加上上下文选择器, 使用空格: 则使得空格前的标签带类选择器成为空格后的标签的父元素*/
        /*也即是说它继承了p,specialtext,p.specialtext三者的样式,这四条都会对span标签产生影响*/
        p.specialtext span {color: blue;}

        .featured {font-size: 5em;}

        /*!!!重点2: 多类选择器*/
        /*(1)先给元素添加一个类,比如h1元素添加featured类,(2)设置多类选择器, 选择同时存在这两个类的元素*/
        .specialtext.featured {color: cadetblue}
```

> 总结：
> 1) CSS中使用空格的, 表示的是选择存在"父/子"关系的元素, 对子元素进行设置样式, 且最终的样式继承父元素样式
> 2) .号本来用来指定类,CSS中使用多个.号的,表示选择同时存在多个类的元素,最终的样式继承这多个类,即 '类1的样式' + '类2的样式'
     

### 2.3 属性选择器
> 根据属性设置样式。

```html
        /*选择带有属性值为title的img设置css*/
        /*下面这句表示忽略title具体值,只要有title属性的img就行*/
        img[title] {border: 2px solid blue;}
        /*下面这句表示只选择title值为nylon的img*/
        img[title="nylon"] {border: 5px solid red;}
```
        
### 2.4伪类
> 伪类分两大种,第一大种为: UI伪类,第二大种为结构化伪类

#### 2.4.1 UI伪类
> 会在HTML元素处于某个状态时(如鼠标指针位于链接上),为该元素应用CSS
1. 链接伪类：
    - a-Link: 链接就在那里等着用户点击
    - a-visited: 用户此前点击过该链接
    - a-hover: 鼠标指针正悬停在链接上
    - a-active: 链接正在被点击,鼠标还没有释放
2. Focus伪类：
    - e:focus{}: e表示h1,p,section,input等html标签,focus类表示鼠标点击时获得焦点
3. target伪类：
    - e:target{}： 如果用户点击一个指向页面中其他元素的链接,则哪个元素就是target,可以用:target选中它
     
#### 2.4.2 结构化伪类
> 结构化伪类可以根据标记的结构应用样式,比如根据某元素的父元素或前面的同胞元素是什么.

`first-child`、`last-child`和`nth-child(n)`代表同一组元素中的第一个元素、最后一个元素和第n个元素。

```html
        /*eg1:链接伪类*/
        p a:link{color: blue}
        p a:visited{color: blueviolet;}
        p a:hover{color: darkgreen;}
        p a:active{color: black;}

        /*eg2: Focus伪类*/
        input:focus{border:2px solid red;}

        /*eg3: target伪类*/
        #img1:target{border: 3px solid red;}
        #img2:target{border: 4px solid green;}


        /*
        eg4:结构化伪类给下面的有序列表1的第一个和第二个表设置CSS样式
        */
        ol.result li:first-child{
            font-style: italic;
            font-size: medium;
            color: red;
        }
        ol.result li:nth-child(2){
            font-size: 26px;
        }
```

### 2.5伪元素
> 伪元素就是若有若无的元素,重点关注几个常用的伪元素,包括first-letter,first-line,before和after

## 3. 定位元素

### 3.1 盒子模型
> 总结：
     1. html中的每个元素都可以看成是一个个盒子的排列，属性border，margin，padding分别制定了盒子的边框，外边距，内边距
     2. width属性指定这个盒子有多大，这个属性非常重要！！！直接影响到后面的外边距margin的设置！！！
     3. margin属性在垂直方向的值会叠加而不是累加！！！为文本元素设置margin的时候通常混合使用单位，上下外边距使用em单位，这样就可以使得段间距随着字号变化而相应增大或者缩小，左右边距使用px

```html
<style>
        p {
            font: 16px Helvetica sans-serif;
            width: 220px;
            border: 2px solid red;
            background-color: #caebff
        }
        p.test {
            margin: 7em 10px;
            padding: 20px;
        }
        p.age {
            margin: 10em 10px;
            padding: 20px;
        }
 </style>
        
         <p class="test">Acoustic guitars have a large hollow body that projects the sound of the strings.</p>
         <p class="age">This is the second paragraph, just show some thing for margin... hope it can help you to understand something</p>


        /*
        总结：
        盒子模型结论1：
            没有设置width的元素始终会扩展到其父元素的宽度，比如上面的p元素没有设置width元素的话，则p的宽度与body的宽度一致。给该元素(p)添加水平边框的宽度(border-width)
            内边距(pading左右值)和外边距（margin左右值）的话，会减少元素的width，减少的width即为水平边框，内边距，外边距之和。
        盒子模型结论2：
            设置了width的元素，添加水平border-width、左右方向的margin与padding时，元素的最终width也会增加。比如上面的例子p添加了width为220px.带标签类p.test
            与p.age分别设置了左右的margin与padding为10px，则p.test/p.age修饰的段落p的width值为：220px+(10+20)*2=260px
        */
```