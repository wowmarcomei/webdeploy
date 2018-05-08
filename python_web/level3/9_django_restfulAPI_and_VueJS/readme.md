#RESTful API与Vue.js配合使用

> 遵循RESTful规则的API，主要包含增删改查：GET,POST,PUT,DELETE，分别对应查，增，改，删。REST风格有如下约定俗成的规定。

1. 网址即为资源。
如：
    - 需要获取网站的全部视频资源，则访问`x.com/videos`.
    - 需要获取全部视频资源中的30个，则给网址添加一个参数如`offset`,访问网址`x.com/videos?offset=30`.
    - 需要访问某个特定视频资源，访问`x.com/videos/1`.

2. 方法对应动作。
    - GET：使用`GET`方法访问`x.com/videos`意味着**获取**这个网址下的全部资源。
    - POST：使用`POST`方法访问`x.com/videos`意味着在当前资源目录下**创建**资源。
    - PUT: 使用`PUT`方法访问`x.com/videos/1`意味着在当前资源目录下**修改**资源。
    - DELETE: 使用`DELETE`方法访问`x.com/videos/1`意味着需要**删除**该资源。

3. 返回响应码。
    - `200`系列：成功。
    - `400`系列：失败。

## 代码实战

### API实现
```python
#website/api.py
@api_view(['GET', 'POST'])
def video(request):
    if request.method == 'GET':
        # 将Video.objects.all()改成按照ID进行逆向排序
        video_list = Video.objects.order_by('-id')
        # 如果需要序列化多个对象，则指定many=True
        serializer = VideoSerializer(video_list, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = VideoSerializer(data=request.data)
        # 类似于表单验证器
        if serializer.is_valid():
            # 序列化器将会直接将数据存储到VideoSerializer中关联的数据库Video
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        # 自定义失败返回码
        body = {
            'body': serializer.errors,
            'msg': '40001'
        }
        return Response(body, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT', 'DELETE'])
def video_card(request, id):
    video_card = Video.objects.get(id=id)
    if request.method == 'PUT':
        serializer = VideoSerializer(video_card, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        video_card.delete()
        return Response({'msg': 'A-OK'}, status=status.HTTP_201_CREATED)
```

### 前端Vue.js实现

### 取消Django渲染，改用Vue.js渲染

使用`{% verbatim %} {% endverbatim %}`来取消Django对Template的渲染，而只使用Vue.js渲染。

参考如下Vue.js的简单实现示例。

```js
<script type="text/javascript">
    var vm = new Vue({
        el: '#app-1',
        data:{   #数据
            message:'hellow vue!!',
            list:[
                { text: 'vegetables'},
                { text: 'potato'},
                { text: 'tomato'},
            ]
        },
        methods:{   #函数
            Name: function(){
                something
            }
        },
        computed:{   #监视器
            filtered:function(){

            }
        },
        transitions:{   #添加过渡效果
            menu:{
                enterClass:'bounceInDown',
                leaveClass:'bounceOutUp'
            },
        },
        ready:function(){    #首先执行
            this.Name()
        }
    })
</script>
```

### 使用`v-show`与`v-on:click`设置是否需要显示下拉菜单

```html
<!-- 菜单栏中的下拉菜单 -->
<div v-show="showMenu" transition="menu" class="ui animated fixed fluid vertical scustom menu">
    <a v-on:click="chozen = 'all'" class="item">All</a>
    <a class="item">Popular</a>
    <a v-on:click="chozen = 'editors_choice' " class="item">Editor</a>
    <a v-on:click="editorMode = !editorMode" class="inverted item"> editorMode </a>
</div>

<!-- 菜单栏 -->
<div  class="ui fixed inverted red borderless menu">
    <!-- 左侧LOGO -->
    <div  v-on:click="showMenu = !showMenu" class="header item">
        <i class="icon tiny ellipsis vertical"></i>
        10MINs
    </div>
    <!-- 右侧 -->
    <div class="right menu">
        <div class="item">
            <button class="ui tiny inverted circular button" type="button" 		name="">Login</button>
        </div>
    </div>

</div>
```

`v-show`基于变量`showMenu`来实时驱动是否需要显示该div，`v-on:click`对变量`showMenu`进行取反，这样就达到了点击菜单栏左侧时，下拉菜单才显示出来。

其中`scustom`为自定义CSS类，只是加了一个距离顶端的绝对距离，实现了点击菜单时，下拉菜单显示出来，且该下拉菜单距离top为50px。

```css
.ui.fixed.scustom.menu {
    position: fixed;top:50px;
 }
```

其中动画效果通过如下代码实现。

```js
new Vue({
  el: '...',
  data: {...},
  transitions:{
                    menu:{
                        // 使用animate.css里定义好的动画bounceInDown与bounceOutUp
                        enterClass:'bounceInDown',
                        leaveClass:'bounceOutUp'
                    },

                },
})
```

重点解释下动画`transition`的使用说明，参考官网的说明[Transitions:](https://v1.vuejs.org/guide/transitions.html)

The `transition` attribute can be used together with: 

- `v-if`
- `v-show`
- `v-for` (triggered for insertion and removal only, for animating changes of order
  [use vue-animated-list plugin](https://github.com/vuejs/vue-animated-list))
- Dynamic components (introduced in the [next section](https://v1.vuejs.org/guide/components.html#Dynamic-Components))
- On a component root node, and triggered via Vue instance DOM methods, e.g. `vm.$appendTo(el)`.

最原始与基本的做法是：自定义所有的动画。当然也有简单的方法，即配合 [Animate.css](https://daneden.github.io/animate.css/)一起使用。

You can specify custom `enterClass` and `leaveClass` in the transition definition. These will override the conventional class names. Useful when you want to combine Vue’s transition system with an existing CSS animation library, e.g. [Animate.css](https://daneden.github.io/animate.css/):

```html
<div v-show="ok" class="animated" transition="bounce">Watch me bounce</div>
```

```js
Vue.transition('bounce', {
  enterClass: 'bounceInLeft',
  leaveClass: 'bounceOutRight'
})
```

### 使用`v-show`与`v-on:click`设置提交表单form

```html
<!-- 弹出提交表单对话框 -->
<!-- 调用animated库模拟渐出场景fadeIn和FadeOut -->
<div v-show="modal.show" class="ui dimmer animated {{ fadeInOut }} active"   >
    <div class="ui padded modal {{ loadingOrNot }} segment active">
        <h3 class="ui header">{{ showMsg }}</h3>
        <i v-on:click="modalSwitch" class="icon tiny close" ></i>

        <div class="content">
            <form >
                <div class="field">
                    <label>this</label>
                    <input v-model="modal.title" type="text" placeholder="title here">
                </div>
                <div class="field">
                    <input v-model="modal.url" type="url" placeholder="cover url">
                </div>
                <div class="field">
                    <input v-model="modal.content" type="text" placeholder="write somthing">
                </div>
            </form>

        </div>
        <!-- 提交表单使用sendData函数 -->
        <div v-on:click="sendData" class="ui fluid positive  button" >Submit</div>
    </div>

</div>
```

```js
new Vue({
  el: '...',
  data: {
  	...
    modal:{
             show:false,
             isLoading:false,
             title:'',
             url:'',
             content:'',
              msg:''
           },
  },
})
```

即在Vue实例中的data中定义一个对象modal，来控制当前的形态。默认`modal.show`为`false`时该表单不显示，否则以弹窗方法显示，使用`SemanticUI`中的`dimmer`与`active`来控制幕布效果（背景为灰，只有对话框为激活状态）。

`<i v-on:click="modalSwitch" class="icon tiny close" ></i>`定义了一个关闭按钮，其关闭对话框的方法为`modalSwitch`.

```js
new Vue({
  el: '...',
  data: {
  	...
    modal:{
             show:false,
             isLoading:false,
             title:'',
             url:'',
             content:'',
              msg:''
           },
  },
  methods:{
            modalSwitch:function () {
            	this.modal.show = !this.modal.show
             },
})
```

提交表单使用sendData函数,定义如下：

```js
new Vue({
  el: '...',
  data: {
  	...
    modal:{
             show:false,
             isLoading:false,
             title:'',
             url:'',
             content:'',
              msg:''
           },
  },
  methods:{
            modalSwitch:function () {
            	this.modal.show = !this.modal.show
             },
            sendData:function () {
   			    var self = this;
                 self.modal.isLoading = !self.modal.isLoading
    			// 使 segment 变成加载状态

    			// 点击submit按钮后将会执行reqwest函数，即使用post方法发送json数据
    			// 如果发送数据成功，则跳入success中，反之跳入error
   				 reqwest({
       				 url:'http://127.0.0.1:8000/api/videos/',
       				 method:'post',
       				 type:'json',
       				 data:{
          				  title:self.modal.title,
          				  url_image:self.modal.url,
          				  content:self.modal.content
       					 },
       				 success:function (resp) {
      			     console.log(resp);
        			 self.modal.isLoading = !self.modal.isLoading
            		 // 如果取回数据成功在把加载状态切换回来
                      self.modal.msg = resp.status
                      // 关闭弹窗
                      self.modalSwitch()
                      // 获取数据
                      self.getData()
                      },
                      error:function (err) {
                      console.log(err);
                      self.modal.msg = err.status
                      self.modal.isLoading = !self.modal.isLoading
                    }
    			}) //end of reqwest函数，reqwest是一个JS库
		}//end of sendData函数
             
}) //end of Vue instance
```

![](http://ww1.sinaimg.cn/large/67c0b572gy1fr40id2ywlj20c10jdgml.jpg)