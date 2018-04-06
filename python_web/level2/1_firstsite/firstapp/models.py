from django.db import models

# Create your models here.
# 创建如下一个类People就等同于在数据库中创建了一个数据表People
class People(models.Model):
    # 在这个数据表中创建字段name,数据类型是char字符；对于类而言，是创建了该类的全局变量
    # null表示数据库中暂时没有这个数据也不会报错，blank表示该字段为空也不会报错，max_length表示最大长度
    name = models.CharField(null=True,blank=True,max_length=200)
    # 定义另外一个字段职位job，也是字符型
    job = models.CharField(null=True,blank=True,max_length=200)