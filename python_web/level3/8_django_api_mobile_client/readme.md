# 获取Django API中json数据采用Vue.js渲染移动端页面

前端使用Vue.js进行渲染，通过API获取后端的`json`数据,达到更便捷的前后端分离。

## 在APP下新建移动端视图函数

```python
#website/mobile_views.py

from django.shortcuts import render

def video_list(request):
    return render(request, 'mobile_list.html', {})
```

此处，上下文为空，即不再使用使用django自身进行渲染模板，相反下面将改用vue.js进行渲染。

## 在模板层新建模板`mobile_list.html`

注意：需要使用`verbatim`标签渲染模板，这样django对`verbatim`包含的这段代码将不再渲染。

```python
{% verbatim %}
	<body>
    ...
    </body>
{% endverbatim %}
```

mobile_list.html的关键代码，使用vue.js进行渲染模板：

```html
<!DOCTYPE html>
{% load staticfiles %}

<html>
	...
    {% verbatim %}
    <body id="app">
        <div v-show="showMenu" transition="menu" class="ui animated fixed fluid vertical something menu " >
            <a v-on:click="chozen = 'all'" class="item">All</a>

            <a class="item">Popular</a>

            <a v-on:click="chozen = 'editors_choice' " class="item">Editor</a>
        </div>


        <div class="ui fixed inverted red borderless menu">
            <div v-on:click="showMenu = !showMenu" class="header item">
                <i class="icon tiny ellipsis vertical"></i>
                10MINs
            </div>

            <div class="right menu">
                <div class="item">
                    <button class="ui tiny inverted circular button" type="button" name="">Login</button>
                </div>
            </div>

        </div>
        <!-- v-if="!opps" -->
        <div class="ui cards"  >

            <div v-for="vid in filtered" class="ui fluid card" >
                <div class="content">
                    <h4 class="header"> {{ vid.title }} </h4>
                    <div class="left floated meta">{{ vid.content|limitBy 30 }}</div>
                </div>
                <div class="image">
                    <img :src="vid.url_image" style="height:200px;object-fit: cover;">
                </div>
                <div class="extra content">
                    <span class="right floated">
                      <i class="heart outline like icon"></i>

                    </span>
                    <i class="comment outline icon"></i> 3
                </div>

                <div class="ui divider"></div>
            </div>

        </div>

        <button id="button" class="btn-floating btn-large red" type="button" name="button">
            <i class="icon small pencil"></i>
        </button>
        
    </body>
    {% endverbatim %}
</html>

```
模板中的数据来源于API，使用`reqwest`获取到API数据。

```js
<script>
    vm = new Vue({
        el:"#app",
        data:{
            showMenu:false,
            chozen:'all',
            vids:[]
        },
        methods:{
            getData:function () {
                var self = this;
                reqwest({
                    url:'http://127.0.0.1:8000/api/video/',
                    // 这里请换成自己的端口，一般是8000
                    type:'json',
                    success:function (resp) {
                        self.vids = resp
                    },

                })
            }
        },
        computed:{
            filtered:function () {
                var self = this
                if (self.chozen == 'editors_choice') {
                    var newList =self.vids.filter(function (vid) {
                            return vid.editors_choice == true
                        })
                    return newList
                } else {
                    return self.vids
                }

            }
        },
        transitions:{
            menu:{
                enterClass:'bounceInDown',
                leaveClass:'bounceOutUp'
            }
        },

        ready:function () {
            this.getData()
        }
    })
</script>
```

## 给view分配url

```python
#urls.py

from website.mobile_views import video_list

urlpatterns = [
    ...
    url(r'^m/videolist/', video_list),
]
```



##效果图

![](https://ws3.sinaimg.cn/large/006tKfTcgy1fr0pmzd9wuj311y0j8abt.jpg)