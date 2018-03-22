"""django_mysite URL Configuration

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

    # 是一連串的規則 (URL patterns)
    # Django 收到 request 時，會一一比對 URL conf 中的規則，決定要執行哪個 view function

"""


from django.conf.urls import url
from django.contrib import admin
from mysite.views import hello_world, home, post_detail


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^hello/$',hello_world), #匹配到hello的时候,就调用hello_world这个view函数
    url(r'^home/',home), #匹配到home主页
    url(r'^post/(?P<pk>\d+)/$',post_detail,name='post_detail')
]

# 以上列表通过函数url(regex, view)来添加,url函数本身有两个参数,第一个为正则表达式,第二个为view函数
# r'^hello/$' 代表的是 hello/ 这种 URL, hello_world对应为views.py下定义的函数