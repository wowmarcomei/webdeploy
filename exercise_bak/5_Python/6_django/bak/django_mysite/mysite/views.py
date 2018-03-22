from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from django.shortcuts import render
from .models import Post

# Create your views here.

# 声明hello_world这个view,传入参数request,返回值为包含字串 Hello World! 的 HttpResponse对象
# 声明完view以后,在urls.py中将url与view相关联起来
# def hello_world(request):
#     return HttpResponse("Hello world!")

# 为了使用模板template,我们改用render函数来回传httpresponse
def hello_world(request):
    return render(request,'hello_world.html',{'current_time':str(datetime.now()),})

def home(request):
    post_list = Post.objects.all()
    return render(request,'home.html',{'post_list': post_list},)

def post_detail(request,pk):
    post = Post.objects.get(pk=pk)
    return render(request,'post.html',{'post':post,})