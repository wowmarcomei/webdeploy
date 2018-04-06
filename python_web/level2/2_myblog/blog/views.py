from django.shortcuts import render, HttpResponse
from django.template import Template, Context
from blog.models import Article

# Create your views here.
def home(request):
    article_set = Article.objects.all()
    context = {
        'template_article':article_set,
    }
    web = render(request,'first_web_2.html',context)
    return web