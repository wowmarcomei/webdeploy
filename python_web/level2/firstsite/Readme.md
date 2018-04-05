## Django初认识

### Models
Models可以理解为数据库Database的总代理，可以对数据库进行`增删改查`。

![](https://ws4.sinaimg.cn/large/006tNc79gy1fpz6jdkblsj30ck0awq36.jpg)

### Templates
负责把从数据库中获得的数据填充进网页中，变成成型的网页，这个过程称之为`渲染`，网页的90%的信息都是从数据库中获取然后进行渲染。

![](https://ws3.sinaimg.cn/large/006tNc79gy1fpz6jck6ooj30a00brdg1.jpg)

### Views
把渲染好的网页返回给使用者，在浏览器中可以看见。

![](https://ws4.sinaimg.cn/large/006tNc79gy1fpz6jd82q3j30bt0bagm1.jpg)

### URLs
访问url时，通过`URLs`找到对应的处理这一流程的`Views`。

![](https://ws4.sinaimg.cn/large/006tNc79gy1fpz6jcvqwmj30aw0but8t.jpg)





### Django 创建步骤

#### 1.P-->创建工程firstsite

```django
django-admin startproject firstsite
```

创建完成之后会在当前目录创建一个名字为firstsite的工程文件夹，如下示意图。

```shell
.
├── firstsite
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── manage.py
```

将工程下的`manage.py`中的`python`改成`python3`(依据个人电脑环境而定)

```django
#!/usr/bin/env python
import os
import sys
```

改为：

```django
#!/usr/bin/env python3
import os
import sys
```

#### 2. A-->创建APP

每个工程里可以有多个APP，比如timeline app，user management app等等。通过如下命令创建app:

```shell
cd firstsite   #进入工程目录
python3 manage.py startapp firstapp #使用manage.py创建app，注意由于我们电脑安装python2与python3，所以每次使用python时，都将其改为python3，防止冲突
```

创建完app后，可以看到工程目录下多了一个firstapp目录。

```shell
.
├── firstapp
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── migrations
│   │   └── __init__.py
│   ├── models.py
│   ├── tests.py
│   └── views.py
├── firstsite
│   ├── __init__.py
│   ├── __pycache__
│   │   ├── __init__.cpython-35.pyc
│   │   └── settings.cpython-35.pyc
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── manage.py

4 directories, 14 files
```

其中`firstsite`下存放的是一些全局设置。

- settings.py：常用的主要设置，包括**添加新的APP**，指定静态文件**CSS，Images，Javascript**，等。
- urls.py: 全局**url入口**设置。

其中`firstapp`下存放的是这个app下的数据。

- models.py：数据库代理。
- admin.py: 管理员设置，注册models。
- views.py: 使用渲染模块**render**，并返回结果。

每次创建一个APP之后，需要在全局settings.py中添加该APP，如下`firstapp`即为本次添加APP。

```python
# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'firstapp', #添加新创建的APP
]
```

#### 3. D-->创建数据库 Database

```shell
python3 manage.py makemigrations
```

生成一个数据库文件`db.sqlite3`

```shell
python3 manage.py migrate
```

合并数据库打印界面如下：

```shell
 meixuhong@MyMac  ~/Desktop/Django/firstsite  python3 manage.py migrate
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, sessions
Running migrations:
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  Applying admin.0001_initial... OK
  Applying admin.0002_logentry_remove_auto_add... OK
  Applying contenttypes.0002_remove_content_type_name... OK
  Applying auth.0002_alter_permission_name_max_length... OK
  Applying auth.0003_alter_user_email_max_length... OK
  Applying auth.0004_alter_user_username_opts... OK
  Applying auth.0005_alter_user_last_login_null... OK
  Applying auth.0006_require_contenttypes_0002... OK
  Applying auth.0007_alter_validators_add_error_messages... OK
  Applying auth.0008_alter_user_username_max_length... OK
  Applying sessions.0001_initial... OK
```

最终生成文件如下：

```shell
.
├── db.sqlite3
├── firstapp
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── migrations
│   │   └── __init__.py
│   ├── models.py
│   ├── tests.py
│   └── views.py
├── firstsite
│   ├── __init__.py
│   ├── __pycache__
│   │   ├── __init__.cpython-35.pyc
│   │   ├── settings.cpython-35.pyc
│   │   └── urls.cpython-35.pyc
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── manage.py

4 directories, 16 files
```

创建完默认数据库以后就可以访问默认站点了。

```shell
python3 manage.py runserver
```

![](https://ws3.sinaimg.cn/large/006tNc79ly1fpzu0oukxwj30oz07c3zo.jpg)

#### 4. M-->设置Models

通过Models模块来操作数据库，包括数据库的表的增删改查。

在firstapp目录下的models.py下定义一个类来创建一个数据库的表。

```python
# 创建如下一个类People就等同于在数据库中创建了一个数据表People
class People(models.Model):
    # 在这个数据表中创建字段name,数据类型是char字符；对于类而言，是创建了该类的全局变量
    # null表示数据库中暂时没有这个数据也不会报错，blank表示该字段为空也不会报错，max_length表示最大长度
    name = models.CharField(null=True,blank=True,max_length=200)
    # 定义另外一个字段职位job，也是字符型
    job = models.CharField(null=True,blank=True,max_length=200)
```

代码中创建完数据表之后需要在终端中使用`manage.py`调用`makemigrations`参数，django将会根据写的代码**创建数据表**`People`, 使用`manage.py`调用`migrate`参数，django将会**合并数据库**。

```shell
meixuhong@MyMac  ~/Desktop/Django/firstsite  python3 manage.py makemigrations
Migrations for 'firstapp':
  firstapp/migrations/0001_initial.py:
    - Create model People
 meixuhong@MyMac  ~/Desktop/Django/firstsite  python3 manage.py migrate
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, firstapp, sessions
Running migrations:
  Applying firstapp.0001_initial... OK
 meixuhong@MyMac  ~/Desktop/Django/firstsite 
```



#### 5. V --> 从Views中获取Models数据

在APP的views.py文件中创建视图函数，从而获得Models中的数据，即获取数据库中的数据表。

```python
# 定义一个函数first_try，传入软参为request(用户发来的请求，暂时不管该参数)
def first_try(request):
    # 创建People类的一个实例化对象man，类初始化的参数即为类的变量
    man = People(name='Spork', job='officer')
    # 创建People的另外一个对象woman
    woman = People(name='Lily', job='Engineer')

    return
```

> 注：此处并没有写完整个函数，等后续动作全部执行完毕再回来添加。

#### 6. T --> Template对数据进行渲染

在view中引入Template，完善views.py函数。

```python
# 添加HttpResponse类
from django.shortcuts import render, HttpResponse
# 从app的models中导入People类，从django模板中导入Context(上下文)与Template(模板)
from firstapp.models import People
from django.template import Context, Template

# Create your views here.

# 定义一个函数first_try，传入软参为request(用户发来的请求，暂时不管该参数)
def first_try(request):
    # 创建People类的一个实例化对象man，类初始化的参数即为类的变量
    # 实例化了下面的对象man以后，即是使用了django的M层Models创建了数据表People的一个数据，且对其进行了初始化
    man = People(name='Spork', job='officer') 
    # 创建People的另外一个对象woman
    woman = People(name='Lily', job='Engineer')

    # 使用template将其渲染到我们的网页中，制作如下的模板（实际上是字符串）
    html_string = '''
         <html>
            <head>
                <meta charset="utf-8">
                <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/semantic-ui/2.2.6/semantic.css" media="screen" title="no title">
                <title>firstapp</title>
            </head>

            <body>
                <h1 class="ui center aligned icon header">
                    <i class="hand spock icon"></i>
                    Hello, {{ man.name }}
                    <p>
                        Hi, {{ woman.name }}! How is it going?
                    </p>
                    <p>
                        Hi, {{ woman.job }}! How is it going?
                    </p>
                </h1>
            </body>
        </html>    
    '''
    # 使用Template类初始化，将字符串html_string变成模板
    t = Template(html_string)
    # 为了将数据库中的数据填充到模板，需要将数据变成上下文，使用Context类将数据表中的数据man变成上下文
    # Context里接收的参数是字典类型数据：字典中的key与模板中的字段必须一致，作为填入对象。字典中的value必须是一个变量，此处为People类的一个实例化对象
    c = Context({'man':man, 'woman':woman })
    # 使用Template的render函数，将上下文c填入到模板t中
    web_page = t.render(c)

    # 返回参数为HttpResponse对象
    return HttpResponse(web_page)
```

#### 7. U -> 在URL中分配网址

在全局urls.py中添加如下代码

```python
from firstapp.views import first_try #在app中views.py下新添加的函数

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^first_try/', first_try), #添加views.py下的函数
]
```

> 上面的url第一个参数是网址，可以随意填写，后面对应的是views.py下面定义的函数，返回结果是一个HttpResponse对象

ok，可以正常访问网页了。

![](https://ws3.sinaimg.cn/large/006tNc79gy1fpzwvkur0tj30w209774b.jpg)



### 总结

> 关键步骤 M—> T —> V —> U

- 其中M指的是通过Models来对数据库中的数据表进行**增删改查**。
- T指的是模板Template，可以想象Template为生活中的一个样板，上面有很多孔，这些孔就是需要填入的上下文`Context`。
- 将Template的`render`函数传入参数`Context的对象`即可完成模板的渲染。
- 渲染都是在Views下面完成的，Template的`render`函数返回值需要作为HttpResponse对象返回。
- 需要在URLs中添加完成网站的寻址操作。



> #### 想象Template就是生活中的一个拼图样板，大括号{{ }}里的东西就是我们需要填入的东西，在Django中这个东西即是上下文Context，Context的参数为字典

