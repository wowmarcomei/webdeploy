from django.shortcuts import render, Http404, redirect,HttpResponse
from website.models import Video
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.template import Context, Template

# Create your views here.
def listing(request,cate=None):
    context = {}
    if cate is None:
        vids_list = Video.objects.all()
    if cate == 'editors':
        vids_list = Video.objects.filter(editors_choice=True)
    else:
        vids_list = Video.objects.all()

    # vids_list = Video.objects.all()
    # 使用分页器进行分页，每页9个数据
    page_robot = Paginator(vids_list,9)
    # 使用GET方法获取URL中的参数page：一般类似于/?page=6
    page_num = request.GET.get('page')

    try:
        vids_list = page_robot.page(page_num)
    except EmptyPage:
        # 加载数据的最后一页
        vids_list = page_robot.page(page_robot.num_pages)
    except PageNotAnInteger:
        # 加载数据的第一页
        vids_list = page_robot.page(1)
    
    context['vids_list'] = vids_list
    return render(request,'listing.html',context)