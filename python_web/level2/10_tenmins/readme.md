# 分页器使用


### 1. Model数据库

```python
class Video(models.Model):
    title = models.CharField(null=True, blank=True, max_length=300)
    content = models.TextField(null=True, blank=True)
    url_image = models.URLField(null=True, blank=True)
    cover = models.FileField(upload_to='cover_image', null=True)
    editors_choice = models.BooleanField(default=False)

    def __str__(self):
        return self.title
```

### 2. Views视图函数

```python
def listing(request):
    context = {}
    vids_list = Video.objects.all()
    # 使用分页器进行分页，每页9个数据
    page_robot = Paginator(vids_list,9)
    # 使用GET方法获取URL中的参数page：一般类似于/?page=6
    page_num = request.GET.get('page')

    try:
        # 加载数据的当前页
        vids_list = page_robot.page(page_num)
    except EmptyPage:
        # 加载数据的最后一页
        vids_list = page_robot.page(page_robot.num_pages)
    except PageNotAnInteger:
        # 加载数据的第一页
        vids_list = page_robot.page(1)
    
    context['vids_list'] = vids_list
    return render(request,'listing.html',context)
```

### 3. URL网址

```python
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', listing, name='list'),
    url(r'^list/$', listing, name='list'),
]
```

> 说明：url中如果有参数/?para='abc'，实际上会与初始视图一起被处理：即localhost:8000/list/与localhost:8000/list/?para=marco均会被listing函数处理。

### 4. Template模板

```html
        <div class="ui basic segment container content"  >

            <div class="ui three column grid">

                {% for vid in vids_list %}
                    <div class="column">
                        <a class="ui fluid card" href="#">
                            <div class="image" >                    
                                  <img src="{{ vid.url_image }}">          
                            </div>
                        </a>

                        <div class="title header" href="#">{{ vid.title|truncatechars:30 }}</div>
                        <i class="icon grey unhide"></i>
                        <span style="color:#bbbbbb">10K</span>
                        <span class="" style="color:rgb(226, 226, 226)">|</span>
                        <i class="icon grey checkmark"></i>
                        <span style="color:#bbbbbb">10 people got it</span>

                    </div>

                {% endfor %}
            </div>
        </div>
```

### 5.Template中使用按钮导航进行翻页

```html

    <div class="ui center aligned very padded vertical segment container">
        <div class="ui pagination menu">
            <!-- 使用模板标签进行判断，如果有前一页则使用a标签进行跳转到前一页 -->
            {% if vids_list.has_previous %}
                <a href="?page={{ vids_list.previous_page_number }}" class="item">
                    <i class="icon red left arrow"></i>
                </a>
            {% else %}
                <a href="?page={{ vids_list.start_index }}" class="disabled item">
                    <i class="icon  left arrow"></i>
                </a>
            {% endif %}
		     <!-- 使用模板标签进行判断，如果有后一页则使用a标签进行跳转到后一页 -->
            {% if  vids_list.has_next %}
                <a href="?page={{ vids_list.next_page_number }}" class="item">
                    <i class="icon red right arrow"></i>
                </a>

            {% else %}

                <a href="?page={{ vids_list.end_index }}" class="disabled item">
                    <i class="icon  right arrow"></i>
                </a>
            {% endif %}

        </div>
    </div>
```



### 6.使用静态文件

可以在APP下面新建一个静态文件目录，如upload

```shell
.
├── db.sqlite3
├── db.sqlite3.bak
├── manage.py
├── tenmins
│   ├── __init__.py
│   ├── __pycache__
│   │   ├── __init__.cpython-35.pyc
│   │   ├── settings.cpython-35.pyc
│   │   ├── urls.cpython-35.pyc
│   │   └── wsgi.cpython-35.pyc
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── upload
│   └── cover_image
│       └── boss-fight-stock-images-photos-free-stuff-on-table.jpg
└── website
    ├── __init__.py
    ├── __pycache__
    │   ├── __init__.cpython-35.pyc
    │   ├── admin.cpython-35.pyc
    │   ├── models.cpython-35.pyc
    │   └── views.cpython-35.pyc
    ├── admin.py
    ├── apps.py
    ├── migrations
    │   ├── 0001_initial.py
    │   ├── __init__.py
    │   └── __pycache__
    │       ├── 0001_initial.cpython-35.pyc
    │       └── __init__.cpython-35.pyc
    ├── models.py
    ├── static
    │   ├── css
    │   │   ├── detail.css
    │   │   ├── list_custom.css
    │   │   ├── semantic.css
    │   │   └── themes
    │   │       └── default
    │   │           └── assets
    │   │               ├── fonts
    │   │               │   ├── icons.eot
    │   │               │   ├── icons.otf
    │   │               │   ├── icons.svg
    │   │               │   ├── icons.ttf
    │   │               │   ├── icons.woff
    │   │               │   └── icons.woff2
    │   │               └── images
    │   │                   └── flags.png
    │   ├── images
    │   │   ├── back2.jpg
    │   │   ├── berries-1546125__340.jpg
    │   │   ├── bremen-town-musicians-1651945__340.jpg
    │   │   ├── cobweb-1630493__340.jpg
    │   │   ├── dachshund-1519374__340.jpg
    │   │   ├── detail.jpg
    │   │   ├── elan-1623088__340.jpg
    │   │   ├── mill-1620440__340.jpg
    │   │   ├── rk5161-1636868__340.jpg
    │   │   ├── sunset-1625073__340.jpg
    │   │   ├── tenlogo.png
    │   │   └── yellowstone-national-park-1581879__340.jpg
    │   └── themes
    │       └── default
    │           └── assets
    │               ├── fonts
    │               │   ├── icons.eot
    │               │   ├── icons.otf
    │               │   ├── icons.svg
    │               │   ├── icons.ttf
    │               │   ├── icons.woff
    │               │   └── icons.woff2
    │               └── images
    │                   └── flags.png
    ├── templates
    │   ├── detail.html
    │   ├── listing.html
    │   └── register_login.html
    ├── tests.py
    ├── upload
    │   ├── cover_image
    │   │   └── boss-fight-stock-images-photos-free-stuff-on-table.jpg
    │   └── profile_image
    │       └── elyse.png
    └── views.py
```

在全局设置文件`setting.py`中加入如下配置：

```python
MEDIA_URL = '/upload/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'upload').replace("//", "/")
```

在url中加入如下配置：

```python
# 导入静态文件需要的库
from django.conf import settings
from django.conf.urls.static import static

# 本地调试时，加载本地静态文件
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

在template中修改关于图片的位置的配置：

添加判断条件，如果数据库中存了本地静态文件位置，则加载本地文件，否则加载数据库中的url对应的image

```html
<div class="image" >
       {% if vid.cover %}
           <img src="/upload/{{ vid.cover }}" >
       {% else %}
           <img src="{{ vid.url_image }}">
       {% endif %}
</div>
```

### 7.分类的使用

#### 7.1在数据库中使用Bool值进行判断分类

```python
editors_choice = models.BooleanField(default=False)
```

表明对象是否为`编辑精选`，如果是则该bool值为真，否则为假。

#### 7.2 在URL中添加分类

```python
url(r'^list/(?P<cate>[A-Za-z]+)$', listing, name='list'),
```

表示url可以匹配到localhost:8080/list/[`任意字母或者组合`]时，将会被传入listing视图函数中处理，这个URL的名字为`list`,`任意字母或者组合`将被保存在参数`cate`中。

所以下一步:

- 需要在listing函数中加入参数`cate`的处理方法。

首先传入形参`cate=None`,然后对`cate`进行判断，如果值为空则默认为全部数据，如果值等于`editors`则挑选出这部分数据，后面处理方式不变。

```python
#website/views.py

# Create your views here.
def listing(request,cate=None):
    context = {}
    if cate is None:
        vids_list = Video.objects.all()
    if cate == 'editors':
        vids_list = Video.objects.filter(editors_choice=True)
    else:
        vids_list = Video.objects.all()

    # vids_list = Video.objects.all()
    # 使用分页器进行分页，每页9个数据
    page_robot = Paginator(vids_list,9)
    # 使用GET方法获取URL中的参数page：一般类似于/?page=6
    page_num = request.GET.get('page')

    try:
        vids_list = page_robot.page(page_num)
    except EmptyPage:
        # 加载数据的最后一页
        vids_list = page_robot.page(page_robot.num_pages)
    except PageNotAnInteger:
        # 加载数据的第一页
        vids_list = page_robot.page(1)
    
    context['vids_list'] = vids_list
    return render(request,'listing.html',context)
```

- 需要在模板中使用href引用url标签

```html
<a class="item" href="{% url 'list' %}editors">
     Editor's
</a>
```

表示点击该a标签时，将会跳转到匹配`url(r'^list/(?P<cate>[A-Za-z]+)$', listing, name='list')`中的`list`这个url+editors，即:`http://127.0.0.1:8000/list/editors`,其中url中的`editors`将会被传入到cate中被listing视图函数处理。



![](http://ww1.sinaimg.cn/large/67c0b572gy1fqk6xskaakj211q0nt0vz.jpg)