from django.db import models

# Create your models here.

class Article(models.Model):
    name = models.CharField(null=True,blank=True, max_length=200)
    content = models.TextField()
    TAG_COICES = (
        ('tech','Tech'), #前面是值，后面的名称
        ('life','Life'),
    )
    tag = models.CharField(null=True,blank=True, max_length=5, choices=TAG_COICES)

    def __str__(self):
        return self.name

class Comment(models.Model):
    name = models.CharField(null=True,blank=True, max_length=50)
    comment = models.TextField()
    def __str__(self):
        return self.comment