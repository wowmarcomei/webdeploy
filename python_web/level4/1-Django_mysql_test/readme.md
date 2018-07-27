# MySQL基本知识

## 1. Excel/MySQL/Django的对比

|      | **Excel** | **MySQL**      | **Django** |
| ---- | --------- | -------------- | ---- |
| 1    | Excel文件 | 数据库文件db   | models.py文件 |
| 2    | Sheet     | 数据库中的表   | models.py中定义的class即是定义的一个表 |
| 3    | Line      | 数据库中的记录 | 查询获取的`QuerySet`就是许多记录的集合 |
| 4    | Column      | 数据库中的字段 | models.py中class定义的属性`Filed`即是定义的一个字段 |

![](http://ww1.sinaimg.cn/large/67c0b572gy1fr42wboiu5j20me0fu75o.jpg)

## 2. 使用Navicat创建一个新的MySQL数据库

### 2.1 创建数据库

1. 首先确保Navicat已经连接上MySQL服务器

2. 在Navicat连接上右键点击新建数据库，填入名称与字符集。

3. 双机Demo进入该数据库，点击新建`数据表`，在出现的`数据表`中添加`字段`，后保存。

![](http://ww1.sinaimg.cn/large/67c0b572gy1fr42wboradj20rq0e8ab8.jpg)

![](http://ww1.sinaimg.cn/large/67c0b572gy1fr42wbpcibj20ob0gvgmp.jpg)

4. 手动添加一个主Key: `id`

![](http://ww1.sinaimg.cn/large/67c0b572gy1fr42wbp7ylj20si0epdgt.jpg)



#Django中使用MySQL

mysql作为开源免费数据库，被广泛使用与支持，已经非常成熟，且并发性能很好，Django对Mysql的支持也非常完善。

## 在Django中配置MySQL

1. 在setting中修改数据库为mysql

```python
DATABASES = {
    'default': {
        # 数据库引擎为mysql
        'ENGINE': 'django.db.backends.mysql',
        # 连接的数据库名称
        'NAME': 'django',
        # 连接的数据库名称与密码
        'USER': 'root',
        'PASSWORD': 'admin',
        # 数据库地址为本地
        'HOST': '127.0.0.1',
        # 本地数据库端口为默认3306
        'PORT': '3306',
    }
}
```

2. 创建mysql数据库

由于上面设置了MySQL数据库为`django`，所以我们需要在MYSQL中手动创建该数据库先。可以使用Navicat直接创建。

3. 在django下执行数据库迁移与合并。

```shell
$ python3 manage.py makemigrations
$ python3 manage.py migrate
```

可以在Navicat上清楚地看到Django给创建了哪些数据表，其中`firstapp_article`是在Models.py自定义的数据库表。目前里面只定义了一个字段`title`。
![](http://ww1.sinaimg.cn/large/67c0b572gy1fr454p9e64j20sl0ii3zu.jpg)

4. 给django创建数据库账号

```
python3 manage.py createsuperuser #输入admin，填写密码即可创建
```

5. 在django后台添加数据

需要先在admin.py下注册数据库，然后登陆后台页面`http://127.0.0.1:8000/admin`添加数据

```python
from firstapp.models import Article

# Register your models here.
admin.site.register(Article)
```

![](http://ww1.sinaimg.cn/large/67c0b572gy1fr45bdbl60j20la0d674i.jpg)



6. 查看主页显示的数据库数据是否加载正确

![](http://ww1.sinaimg.cn/large/67c0b572gy1fr4551w633j20pb06fq2t.jpg)

7. Navicat查询数据库数据是否匹配

![](http://ww1.sinaimg.cn/large/67c0b572gy1fr45bu07elj20m70fc3z9.jpg)



## Django中Model与MySQL的关系

实际的数据库中我们可以有多种关系，比如`一对一`,`一对多`,`多对一`与`多对多`。如果定义一个评论类`Comment`与文章类`Article`，那么一个`Article` 可以对应一个`Comment`，也可以设置为对应多个`Comment` ，反之`Comment`也可以。

> 实际上在Django数据库模型中，没有`一对多`关系，只有`多对一`模型。 

1. 在Django中设计`一对一`关系数据库。

```python
#models.py

from django.contrib.auth.models import User

class UserProfile(models.Model):
    # Django会把belong_to变成belong_to_id字段，
    # belong_to_id字段与User中的id字段唯一对应
    belong_to = models.OneToOneField(to=User,on_delete=models.CASCADE,null=True)
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name
```

使用**OneToOneField**来定义,django会将数据库中的表`UserProfile`定义如下字段：

- id：主键
- name
- belong_to_id, 作为**外键**与User的id关联。

![](http://ww1.sinaimg.cn/large/67c0b572gy1fr5dz7qmsyj20sf0f175h.jpg)



2. 在Django中设计`多对一`模型。

```python
class Article(models.Model):
    # 一个用户可以用多个Article，所以使用外键ForeignKey定义多对一，即多个Article对应一个UserProfile
    # 定义了ForeignKey以后，Django会把author字段改成author_id字段
    # 通过author_id来与UserProfile的id关联，多个author_id可对应一个UserProfile的id
    author = models.ForeignKey(to=UserProfile,on_delete=models.CASCADE,related_name='articles',null=True)
    title = models.CharField(max_length=100)
    content = models.TextField(null=True)
    like_counts = models.IntegerField(default=0)
    score = models.FloatField(default=1.1)
    create_time = models.DateField(auto_now=True)

    def __str__(self):
        return self.title
```

使用**ForeignKey**来定义，Django会将`Article`定义如下字段：

- id：主键
- author_id，作为**外键**与User的id关联。
- title
- content
- like_counts
- score
- create_time



3. 在Django中设计`多对多`模型。

```python
class Book(models.Model):
    name = models.CharField(max_length=20,null=True,blank=True)
    authors = models.ManyToManyField(to=Article)

    def __str__(self):
        return self.name
```

首先Django会将`Book`定义如下字段：

- id：主键
- name

然后Django会使用**ManyToManyField**来定义`多对多`模型，将创建一个新表`book_authors`,其中有两个字段：

- id:主键
- book_id: 作为ForeignKey关联到book表中的`id`字段
- article_id：作为ForeignKey关联到article表中的`id`字段

![](http://ww1.sinaimg.cn/large/67c0b572gy1fr5e03r4cjj20rx0gyta0.jpg)