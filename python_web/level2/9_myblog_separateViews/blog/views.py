from django.shortcuts import render, HttpResponse
from django.template import Template, Context
from blog.models import Article, Comment
from blog.form import CommentForm
from django.shortcuts import redirect

# Create your views here.
def home(request):
    # 调试查看request是什么参数，包括值，所有属性与方法，类型
    # print(request)
    # print("==="*30)
    # print(dir(request))
    # print("==="*30)
    # print(type(request))
    # print("==="*30)
    # print(request.GET)
    # print("==="*30)
    queryset = request.GET.get('tag') #通过GET方法获取参数tag的具体值，在url中输入?tag=test123,则此处获取的queryset即为test123
    # print(queryset)
    

    if queryset:   #如果不为空，即传递tag值，则加载分类页面
        article_set = Article.objects.filter(tag=queryset) #过滤出'tag值'为'url中传递的参数'的所有数据表
    else:          #如果为空，即加载所有数据页面
        article_set = Article.objects.all()

    context = {
        'template_article':article_set,
    }
    web = render(request,'first_web_2.html',context)
    return web

# 第二个参数page_num是通过URL中识别传递过来
def details_view(request,page_num):
    context = {}
    # comments_set = Comment.objects.all()
    article = Article.objects.get(id=page_num)

    if request.method == 'GET':
        form = CommentForm  #实例化一个CommentForm
    if request.method == 'POST': #提交表单form时都是使用的POST方法
        form = CommentForm(request.POST)   #1:绑定表单:将请求的POST数据装载在CommentForm实例中，只有在绑定了表单才可以验证数据
        # 2.验证表单：验证表单是否通过，如果通过则进行下面操作，表单数据会被存储在字典变量中
        if form.is_valid():
            name = form.cleaned_data['name'] #取出表单中完成验证的数据（字典变量），将字典中key值为name的变量存储在name中
            comment = form.cleaned_data['comment'] #取出表单中完成验证的数据（字典变量），将字典中key值为comment的变量存储在comment中
            c = Comment(name=name,comment=comment,belong_to=article) #实例化Comment类，初始化其两个变量
            c.save() #存储到数据库中
            return redirect(to='details_page',page_num=page_num) #跳转到url.py中name=details_page的URL中,
            # page_num=page_num表示重定向到当前页，如果设置page_num=3，表示将会跳转到`http://127.0.0.1:8000/details/3`

    
    best_comment = Comment.objects.filter(best_comment=True,belong_to=article)
    # 如果存在最优评论，则将其存入字典中
    if best_comment:
        context['best_comment']=best_comment[0]
    # context['comments_set'] = comments_set
    context['form'] = form #将表单填入到上下文
    context['article'] = article

    return render(request,'detail.html',context)

# 正常文章与历史评论视图
def article_history_comment_view(request,page_num,error_form=None):
    context = {}
    form = CommentForm  #实例化一个CommentForm
    article = Article.objects.get(id=page_num)
    if error_form is not None:
        context['form'] = error_form #将表单填入到上下文
    else:
        context['form'] = form
    context['article'] = article

    best_comment = Comment.objects.filter(best_comment=True,belong_to=article)
    # 如果存在最优评论，则将其存入字典中
    if best_comment:
        context['best_comment']=best_comment[0]

    return render(request,'detail.html',context)

# 提交评论到Comment的视图
def post_form_view(request,page_num):
    form = CommentForm(request.POST)   #1:绑定表单:将请求的POST数据装载在CommentForm实例中，只有在绑定了表单才可以验证数据
    # 2.验证表单：验证表单是否通过，如果通过则进行下面操作，表单数据会被存储在字典变量中
    if form.is_valid():
        name = form.cleaned_data['name'] #取出表单中完成验证的数据（字典变量），将字典中key值为name的变量存储在name中
        comment = form.cleaned_data['comment'] #取出表单中完成验证的数据（字典变量），将字典中key值为comment的变量存储在comment中
        article = Article.objects.get(id=page_num)
        c = Comment(name=name,comment=comment,belong_to=article) #实例化Comment类，初始化其两个变量
        c.save() #存储到数据库中
    else:
        # 如果表单验证不通过，则将这个错误的form传递到上面的article_history_comment_view中展示,
        return article_history_comment_view(request,page_num,error_form=form)
    return redirect(to='details_page',page_num=page_num) #跳转到url.py中name=details_page的URL中,
    # page_num=page_num表示重定向到当前页，如果设置page_num=3，表示将会跳转到`http://127.0.0.1:8000/details/3`