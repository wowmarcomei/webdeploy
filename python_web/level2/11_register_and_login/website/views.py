from django.shortcuts import render, Http404, redirect,HttpResponse
from website.models import Video
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.template import Context, Template
# 引入鉴权与登陆模块authenticate,login
from django.contrib.auth import authenticate,login
# 引入自定义的登陆用的表单
from website.form import LoginForm
# 引入Django核心表单模块，用于登陆与注册使用
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm

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

# 使用自定义表单进行登陆验证
def index_login_bak(request):
    # 定义模板字典
    context = {}
    if request.method == 'GET':
        # 构造并渲染表单,使用自定义的表单
        form = LoginForm

    if request.method == 'POST':
        # 获取表单数据
        form = LoginForm(request.POST)
        if form.is_valid():
            # 使用cleaned_data取出验证后的用户名与密码
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            # 对用户名密码进行鉴权
            user = authenticate(username=username,password=password)
            if user:
                # 如果用户通过鉴权，则进行登陆，将其重定向到url名字为list的页面
                login(request,user)
                return redirect(to='list')
            else:
                return HttpResponse('<h1>Not a user!</h1>')
    #GET方法时渲染的表单，在'register_login.html'中进行渲染 
    context['form'] = form
    return render(request,'register_login.html',context)

# 使用Django自带的AuthenticationForm表单进行登陆
def index_login(request):
    # 定义模板字典
    context = {}
    if request.method == 'GET':
        # 构造并渲染表单
        form = AuthenticationForm

    if request.method == 'POST':
        # 获取表单数据
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request,form.get_user())
            return redirect(to='list')
            
    #GET方法时渲染的表单，在'register_login.html'中进行渲染 
    context['form'] = form
    return render(request,'register_login.html',context)

# 使用Django自带的UserCreationForm表单进行注册
def index_register(request):
    # 定义模板字典
    context = {}
    if request.method == 'GET':
        # 构造并渲染表单
        form = UserCreationForm

    if request.method == 'POST':
        # 获取表单数据
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='login')
            
    #GET方法时渲染的表单，在'register_login.html'中进行渲染 
    context['form'] = form
    return render(request,'register_login.html',context)