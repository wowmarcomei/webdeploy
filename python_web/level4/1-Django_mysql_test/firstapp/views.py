from django.shortcuts import render
from firstapp.models import Article

# Create your views here.
def home(request):
    article_set = Article.objects.all()
    context = {}
    context['article_set'] = article_set

    return render(request,'index.html',context)