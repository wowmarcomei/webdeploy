### models参数

Django中使用choices参数传递分类，其中choices是一个元祖变量，里面可以存放多个选项，每个选项中第一个值为程序中变量，第二个值为在数据库后台看到的名称

```python
TAG_COICES = (
        ('tech','Tech'), #前面是值，后面的名称
        ('life','Life'),
    )
tag = models.CharField(null=True,blank=True, max_length=5, choices=TAG_COICES)
```

### request请求

request请求是一个http请求，可以通过如下方法打印出request的信息。

```python
print(request)
    print("==="*30)
    print(dir(request))
    print("==="*30)
    print(type(request))
    print("==="*30)
    print(request.GET)
    print("==="*30)
    queryset = request.GET.get('tag') #通过GET方法获取参数tag的具体值，在url中输入?tag=test123,则此处获取的queryset即为test123
    print(queryset)
```

其中`dir(request)`获取到request的全部属性与方法，`request.GET`返回一个QueryDict，字典变量的`key`值即为url中输入的值，如`http://127.0.0.1:8000/home/?tag=life`中的tag，`value`值为life。

如当访问上面的网址时，将在控制台打印出如下日志：

```shell
<WSGIRequest: GET '/home/?tag=life'>
==========================================================================================
['COOKIES', 'FILES', 'GET', 'META', 'POST', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__iter__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_encoding', '_get_files', '_get_post', '_get_raw_host', '_get_scheme', '_initialize_handlers', '_load_post_and_files', '_mark_post_parse_error', '_messages', '_post_parse_error', '_read_started', '_set_post', '_stream', '_upload_handlers', 'body', 'build_absolute_uri', 'close', 'content_params', 'content_type', 'csrf_processing_done', 'encoding', 'environ', 'get_full_path', 'get_host', 'get_port', 'get_raw_uri', 'get_signed_cookie', 'is_ajax', 'is_secure', 'method', 'parse_file_upload', 'path', 'path_info', 'read', 'readline', 'readlines', 'resolver_match', 'scheme', 'session', 'upload_handlers', 'user', 'xreadlines']
==========================================================================================
<class 'django.core.handlers.wsgi.WSGIRequest'>
==========================================================================================
<QueryDict: {'tag': ['life']}>
==========================================================================================
life
[09/Apr/2018 01:28:22] "GET /home/?tag=life HTTP/1.1" 200 4623
```

![](https://ws4.sinaimg.cn/large/006tKfTcgy1fq65248tl7j30si0itdgs.jpg)



![](https://ws2.sinaimg.cn/large/006tKfTcgy1fq6522sb1xj30sj0j1gmj.jpg)