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

1. 创建工程firstsite: **P**

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

2. 创建APP : **A**

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

3. 创建数据库 database：**D**

```shell
python3 manage.py makemigrations
```

生成一个数据库文件`db.sqlite3`

```shell
python3 manage.py migrate
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

