# Django中写API

##基本原理

用`Models`与`Views`返回一个给`Template`(Vue.js)使用的`json`数据: 访问网址返回`json`.

需要哪些步骤：

1. 需要将`Models`中的数据进行**序列化**成**字典**。

![](https://ws4.sinaimg.cn/large/006tKfTcgy1fr0lsq1xn0j30dq039q33.jpg)

Python中的字典结构与Json几乎是一致的，都是键值对`{key:value}`。序列化指的就是将这些数据全部放入列表中变成：

```js
[
    {key:value},
    {key:value},
    {key:value},
]
```

即是将数据变成列表，列表中是字典数据。

2. 将字典变成`json`.

![](https://ws4.sinaimg.cn/large/006tKfTcly1fr0lxkncgtj30dp02emx6.jpg)

返还给前端使用的数据必须是`json`格式数据，所以必须要转换格式。

## 代码实例

1.安装插件`djangorestframework`

```shell
pip3 install djangorestframework
```

2.在`settings.py`中引用该插件

```python
# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'website',
    # 安装完插件“djangorestframework” 后需要添加该插件才能仅需使用
    'rest_framework',
]
```

3. 在APP下新建一个`api.py`文件，引入所需要的库

> 注：其与models.py和views.py同级别

```python
# 引入Models数据库
from website.models import Video
# 引入rest_framework中的序列化需要的库,构造序列化器，将models中的数据转换成字典结构
from rest_framework import serializers
# 引入rest_framework中的响应库与api_view,让视图只返回json数据
from rest_framework.response import Response
from rest_framework.decorators import api_view
```

4. 构建序列化，定义一个序列化器类


```python
#website/api.py

# 1.构建序列化，定义一个序列化器类
class VideoSerializer(serialzers.ModelSerializer):
    # 定义一个类Meta，这是序列化的固定写法
    class Meta:
        # 需要序列化的类为Video
        model = Video
        # 定义为__all__以后，后续会将数据库中所有数据都转换为字典结构，包括以下几个：
        # title，content，url_image，cover和editors_choice
        fields = '__all__'
        # 如果只需要转换其中一部分的话，可以使用元祖来定义，如只需转换title和content的话可以按照如下定义
        # 注意：后面一个数据后的逗号不能少
        # fields = ('title','content',)
```

5. 编写视图函数，将字典数据转换为json数据

```python
#website/api.py

# 2.编写一个视图,且添加装饰器使得返回的Response里的数据真正转化为json数据
# 装饰器的作用即是装饰某个函数，可以理解为该函数的插件，下面语句指的是使用GET方法访问时可以返回json数据
@api_view(['GET'])
def vidoe(request):
    # 获取所有数据库Video的所有对象，返回结果为QuerySet
    video_list = Video.objects.all()
    # 实例化一个序列化器，传入参数为获取的QuerySet即查询的所有数据库对象实体
    # 第二个参数many=True表示的是对所有数据进行序列化，如果取回的数据只有一个对象则不需要指定many
    serializer = VideoSerializer(video_list,many=True)

    return Response(serializer.data)
```

6. 给视图函数video分配一个url

```python
#urls.py

from website.api import video

urlpatterns = [
    ...
    url(r'^api/video/', video),
]

```

测试api视图：

![](https://ws4.sinaimg.cn/large/006tKfTcgy1fr0otk6iqzj311y0jpwf8.jpg)



关于序列化器可以参考官网：http://www.django-rest-framework.org/api-guide/serializers/#modelserializer

