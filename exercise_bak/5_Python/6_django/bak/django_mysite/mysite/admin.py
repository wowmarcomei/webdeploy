from django.contrib import admin

# 最後，我們需要在讓 Django 知道，有哪些 Model 需要管理後台。
# 修改 mysite app 裡的 admin.py，並註冊 Post 這個 Model：
from .models import Post

# Register your models here.

admin.site.register(Post)