from django.shortcuts import render

# Create your views here. 视图层,进行控制与访问数据库控制Module

def index(request):
    '''
    调用template的view函数
    :param request:
    :return:
    '''
    return render(request,'index.html')