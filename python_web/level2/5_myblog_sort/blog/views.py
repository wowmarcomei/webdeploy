from django.shortcuts import render, HttpResponse
from django.template import Template, Context
from blog.models import Article

# Create your views here.
def home(request):
    # 调试查看request是什么参数，包括值，所有属性与方法，类型
    print(request)
    print("==="*30)
    print(dir(request))
    print("==="*30)
    print(type(request))
    print("==="*30)
    print(request.GET)
    print("==="*30)
    queryset = request.GET.get('tag') #通过GET方法获取参数tag的具体值，在url中输入?tag=test123,则此处获取的queryset即为test123
    print(queryset)
    

    if queryset:   #如果不为空，即传递tag值，则加载分类页面
        article_set = Article.objects.filter(tag=queryset) #过滤出'tag值'为'url中传递的参数'的所有数据表
    else:          #如果为空，即加载所有数据页面
        article_set = Article.objects.all()

    context = {
        'template_article':article_set,
    }
    web = render(request,'first_web_2.html',context)
    return web