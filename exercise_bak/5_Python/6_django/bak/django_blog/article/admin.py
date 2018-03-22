from django.contrib import admin

# 增加本APP添加的数据库
from article.models import Article

# Register your models here.
admin.site.register(Article)
