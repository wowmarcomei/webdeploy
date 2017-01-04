"""my_blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from article.views import home,detail,test
import article

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^home/$',home,name='home'),
    url(r'',home,name='home'),
    # 这是第一个坑,总结一下
    # 1.尖括号中的参数会传给detail函数作为其形参, 2.name传递给模板中html文件,用于构造django模板语言
    url(r'^(?P<my_args>\d+)/$',detail,name='detail_template'),
    url(r'^test/$',test,name='test'),

    # url(r'^$', 'article.views.home', name = 'home'),
    # url(r'^(?P<id>\d+)/$', 'article.views.detail', name='detail'),
    # url(r'^archives/$', 'article.views.archives', name = 'archives'),
    # url(r'^aboutme/$', 'article.views.about_me', name = 'about_me'),
    # url(r'^tag/(?P<tag>\w+)/$', 'article.views.search_tag', name = 'search_tag'),
    # url(r'^search/$','article.views.blog_search', name = 'search'),
    # url(r'^feed/$', RSSFeed(), name = "RSS"),
]
