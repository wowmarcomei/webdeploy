"""django_blog URL Configuration

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
from article.views import home_test,detail,test,home

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # 下叙正则表达式是获取数字传给my_args,这个变量传给detail
    # ?P为命名抓取组: (?P<name>regex)-匹配regex里的正则,然后被name引用(即传值给name)
    # 详细描述: https://docs.djangoproject.com/en/1.10/topics/http/urls/
    # 第三个参数name是为了给template使用
    # url(r'^(?P<my_args>\d+)/$',detail,name='detail'),
    url(r'^test/',test),
    url(r'^home_test/',home_test),
    url(r'^home/',home),
    url(r'^(?P<id>\d+)/$',detail,name='detail')
]
