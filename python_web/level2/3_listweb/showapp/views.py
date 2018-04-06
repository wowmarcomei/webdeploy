from django.shortcuts import render,HttpResponse
from showapp.models import waterfall
from django.template import Template, Context

# Create your views here.
def index(request):
    img_set = waterfall.objects.all()
    context = {
        'template_img_set': img_set,
    }
    web = render(request,'list.html',context)
    return web