### 分离视图

1. 分离文章与表单视图

```python
# blog/views.py

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
```

2. 分离URL

```python
# blog/urls.py
from blog.views import home, details_view,article_history_comment_view,post_form_view

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^home/', home, name=None),
    url(r'^details/(?P<page_num>\d+)$', article_history_comment_view, name='details_page'), 
    url(r'^details/(?P<page_num>\d+)/comment$', post_form_view, name='comment'), 
]
```

3. template中更新form的action

`action`指定`form`提交到哪个网址，可以使用url标签来进行。

```html
<form class="ui error tiny form" action="{% url 'comment' article.id %}" method="post">
...
</form>
```

> - 给form添加一个action到新的地址，地址通过url标签来表示
> - 结合urls.py中定义 `url(r'^details/(?P<page_num>\d+)/comment$', post_form_view, name='comment')`可知: 一旦在这个页面提交了表单，则表单提交到了`details/article.id/comment`这个页面下,如下截图所示：

评论页面：
![](http://ww1.sinaimg.cn/large/67c0b572gy1fqa40bzmwcj211y0k87bt.jpg)

文章与历史评论页面：
![](http://ww1.sinaimg.cn/large/67c0b572gy1fqa40i0cd1j211y0k8aid.jpg)



