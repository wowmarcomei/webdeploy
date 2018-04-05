### 1. 加载静态模板templates

- 在APP目录下新建templates目录，里面放入html模板
- 在APP目录下新建static目录，里面放入css, images, theme等静态文件
- 在全局setting.py目录下修改列表变量TEMPLATES

```python
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates').replace('\\', '/')], #修改DIR
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```

- 在templates目录下的html文件中使用模板语言即可引用静态文件与django的变量

> 1）引用静态文件：{% load staticfiles %}，后续有引用路径时，全部使用模板语言替换，如

```html
<link rel="stylesheet" href="css/semantic.css"  media="screen" title="no title" charset="utf-8">
```

改成：

```html
<link rel="stylesheet" href="{% static 'css/semantic.css' %}"  media="screen" title="no title" charset="utf-8">
```

> 2）使用数据库中的数据填写模板中内容。

> 3)  在views.py中引用上面的html模板时，直接可以写入在render函数中写入名称即可，如：

```python
render(request, 'first_web_2.html', context) #first_web_2.html即是在templates下的html文件
```



### 2. 创建数据库账号

```shell
python3 manage.py createsuperuser #输入admin，填写密码即可创建
```

需要修改数据库的话，在app的models.py下面增加新的类即可，如：

```python
class Article(models.Model):
    headline = models.CharField(null=True,blank=True,max_length=200)
    content = models.TextField()

    def __str__(self):	#定义一个函数，返回对象的变量headline
        return self.headline
```

### 3. 注册数据表

需要在admin.py下使用如下语句注册已经通过Django创建的数据表table, 

```python
admin.site.register(Article) #注册数据表Article
```

### 4. 定义views视图函数

在views.py下面定义views视图函数，比如希望访问localhost:8000/home，则需要在views.py下定义home函数，传入参数为request。

```python
# Create your views here.
def home(request):
    article_set = Article.objects.all()
    context = {
        'template_article':article_set,
    }
    web = render(request,'first_web_2.html',context)
    return web
```

上面这段函数中最难理解是article_set的定义与context的定义。

- article_set即是一个QuerySet，顾名思义，其实就是我们在models中实现的**数据表的集合**，要想取得它的具体值，必须使用**迭代**，如：

```python
for a in article_set:
    print(a.xxxxx)
```

- context是一个字典，之所以定义字典是因为Django的模板Template只接收字典类数据作为变量。上面的context赋值以后，有**一个**key值为`template_article`,这个key值对应的value就是上面的数据表集合QuerySet类型数据`article_set`。
- 后面在Template(即xxx.html)文件中的上下文必须使用迭代才能访问到数据表的具体值，且`模板中变量名`与上述home函数中定义的`key值`必须完全一致才能匹配。

```html
{% for article in template_article %}
	{{article.name }}
{% endfor %}
```



![](http://ww1.sinaimg.cn/large/67c0b572ly1fq27engy5sj20wc18n0x4.jpg)