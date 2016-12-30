from django.shortcuts import render
from django.http import HttpResponse
from article.models import Article
# Create your views here.
def home(request):
    return HttpResponse("Hello,world,django.")

def detail(request, my_args):
    # return HttpResponse("You're looking at my_args {}.".format(my_args))
    post = Article.objects.all()[int(my_args)]
    str = ("title={},category={},date_time={},content={}".format(post.title,post.category,post.date_time,post.content))
    return HttpResponse(str)