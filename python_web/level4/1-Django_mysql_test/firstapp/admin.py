from django.contrib import admin
from firstapp.models import Article,UserProfile,Book

# Register your models here.
admin.site.register(Article)
admin.site.register(UserProfile)
admin.site.register(Book)