from django.contrib import admin

# Register your models here.

from .models import Article,Category

# Register your models here.
admin.site.register(Article)
admin.site.register(Category)