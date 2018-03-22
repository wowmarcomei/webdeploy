# 处理数据库
from django.db import models

# Create your models here.

# 创建一个post类,并定义属性,Django会根据这个建立资料表,以及对应资料表的设定
class Post(models.Model):
    title = models.CharField(max_length=100)  #字符串类型,长度不超过100
    content = models.TextField(blank=True)    #文本内容类型,非必填栏(表单验证时使用)
    photo = models.URLField(blank=True)       #链接类型,非必填栏
    location = models.CharField(max_length=100) #字符串类型,长度不超过100
    created_at = models.DateTimeField(auto_now_add=True) #时间类型,auto_now_add = True表示新增的时间

    def __str__(self):
        '''
        Django 通常以 Post object 來表示 Post 物件，但此種顯示不易辨別。我們可以透過 def __str__ 更改 Post 的表示方式。
        :return: self.title
        '''
        return self.title

# 创建完类Post之后,使用命令 python3 manage.py makemigrations会根据对models.py的修改建立一个新的migration记录
# 然后使用命令 pythons manage.py migrate,让Django 根据上面的记录，把 models.py 中的数据写入数据库

