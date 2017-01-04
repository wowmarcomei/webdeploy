from django.shortcuts import render
from django.http import HttpResponse
from article.models import Article
from datetime import datetime
from django.http import Http404

# Create your views here.

def home(request):
    # Test 1: 简单显示Hello world
    # return HttpResponse("Hello World, Django")
    post_list = Article.objects.all()
    return render(request,'home.html',{'post_list':post_list})

def detail(request,my_args):
    # ---Test1: 直接调用传入的软参 my_args
    # return HttpResponse("You're looking at my_args {}.".format(my_args))
    # ---Test2: 访问数据库
    # post = Article.objects.all()[int(my_args)]
    # str = ("title={}, category={}, date_time={},content={}.".format(post.title,post.category,post.date_time,post.content))
    # return HttpResponse(str)
    # ---Test3: 动态URL
    try:
        post = Article.objects.get(id=str(my_args))
    except Article.DoesNotExist:
        raise Http404
    return render(request,'post.html',{'post':post})

def test(request):
    # render函数的有很多默认参数,前两个是必须的,第三个参数content为字典:https://docs.djangoproject.com/en/1.8/topics/http/shortcuts/#render
    # 即request参数解析为一个http response,结果传给第二个参数test.html,第三个参数作为其中一个内容也传给第二个参数
    return render(request,'test.html',{'current_time':datetime.now()})

