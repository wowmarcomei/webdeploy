from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    # Django会把belong_to变成belong_to_id字段，
    # belong_to_id字段与User中的id字段唯一对应
    belong_to = models.OneToOneField(to=User,on_delete=models.CASCADE,null=True)
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name

# Create your models here.
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

class Book(models.Model):
    name = models.CharField(max_length=20,null=True,blank=True)
    authors = models.ManyToManyField(to=Article)

    def __str__(self):
        return self.name