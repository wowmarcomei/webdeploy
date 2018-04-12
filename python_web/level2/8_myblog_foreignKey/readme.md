### 如何关联数据库

如何将评论分别显示在每个文章下，而不是将每篇文章下都显示全部的评论？

一开始在设计数据库的时候，文章Article Class与评论Comment Class是独立的数据库类，并没有关联。而实际的数据库中我们可以有多种关系，比如`一对一`,`一对多`,`多对一`与`多对多`。即是说一个Article 可以对应一个Comment，也可以设置为对应多个Comment ，反之Comment也可以。

> 实际上在Django数据库模型中，没有`一对多`关系，只有`多对一`模型。

所以为了实现将多个评论唯一地展现在某一篇文章下面，我们可以使用Django数据库模型中的`多对一`模型。在Comment类中添加ForeignKey即可将多个Comment关联到一个Article中。

```python
# blog/models.py
class Article(models.Model):
    name = models.CharField(null=True,blank=True, max_length=200)
    content = models.TextField()
    TAG_COICES = (
        ('tech','Tech'), #前面是值，后面的名称
        ('life','Life'),
    )
    tag = models.CharField(null=True,blank=True, max_length=5, choices=TAG_COICES)

    def __str__(self):
        return self.name

class Comment(models.Model):
    name = models.CharField(null=True,blank=True, max_length=50)
    comment = models.TextField()
    belong_to = models.ForeignKey(to=Article,related_name="under_comments",on_delete=models.CASCADE,null=True,blank=True)
    def __str__(self):
        return self.comment
```

其中`belong_to = models.ForeignKey(to=Article,related_name="under_comments",on_delete=models.CASCADE,null=True,blank=True)` 就是创建`Comment`与`Article`的对应关系，在评论类中指明其外键ForeignKey为Article，参数`related_name="under_comments"`表示可以在`Article`中通过`under_comments`来引用`Comments`。

#### 方法1：Article对象引用Comment对象

修改view视图函数：

```python
# blog/views.py
# 第二个参数page_num是通过URL中识别传递过来
def details_view(request,page_num):
    if request.method == 'GET':
        form = CommentForm  #实例化一个CommentForm
    if request.method == 'POST': #提交表单form时都是使用的POST方法
        form = CommentForm(request.POST)   #1:绑定表单:将请求的POST数据装载在CommentForm实例中，只有在绑定了表单才可以验证数据
        # 2.验证表单：验证表单是否通过，如果通过则进行下面操作，表单数据会被存储在字典变量中
        if form.is_valid():
            name = form.cleaned_data['name'] #取出表单中完成验证的数据（字典变量），将字典中key值为name的变量存储在name中
            comment = form.cleaned_data['comment'] #取出表单中完成验证的数据（字典变量），将字典中key值为comment的变量存储在comment中
            c = Comment(name=name,comment=comment) #实例化Comment类，初始化其两个变量
            c.save() #存储到数据库中
            return redirect(to='details_page') #跳转到url.py中name=details_page的URL中

    context = {}
    # comments_set = Comment.objects.all()
    article = Article.objects.get(id=page_num)
    # context['comments_set'] = comments_set
    context['form'] = form #将表单填入到上下文
    context['article'] = article

    return render(request,'detail.html',context)
```

即取消掉`comments_set`的定义，同时注释掉字典中对应`comments_set`的key值定义。

```python
# comments_set = Comment.objects.all()
# context['comments_set'] = comments_set
```

由于取消了这个字典的定义，那么在模板template的文件`detail.html`中不能再引用变量`comments_set`，而直接通过`Article`这个类来引用`Comments`类：

将如下语句进行更换：

```django
<!-- detail.html -->
{% for comment in comments_set %}
```

改成：

```django
<!-- detail.html -->
{% for comment in article.under_comments.all %}
```

其中`under_comments`即为在数据库Models中定义的变量名，同时记得一定要加`.all`使其变成`QuerySet`变量才能进行迭代。即在view视图中变成：

`Article.objects.get(id=page_num).under_comments.all`

#### 方法2：Comment对象引用Article对象

为了做这个测试，先在数据库中给Comment添加一个是否是最优评论的Bool变量。

```python
# blog/models.py
class Comment(models.Model):
    name = models.CharField(null=True,blank=True, max_length=50)
    comment = models.TextField()
    belong_to = models.ForeignKey(to=Article,related_name="under_comments",on_delete=models.CASCADE,null=True,blank=True)
    #添加下面的best_comment
    best_comment = models.BooleanField(default = False)
    def __str__(self):
        return self.comment
```

添加变量`best_comment`后进行数据库合并。

```shell
$ python3 manage.py makemigrations
$ python3 manage.py migrate
```

登录数据库后台可以看到已经成功添加是否为最佳评论。

![](http://ww1.sinaimg.cn/large/67c0b572gy1fq9zymbyntj20ns0dlmxf.jpg)

在view视图函数中修改，通过comment对象直接引用article对象。添加如下代码：

```python
	best_comment = Comment.objects.filter(best_comment=True,belong_to=article)
    # 如果存在最优评论，则将其存入字典中
    if best_comment:
        context['best_comment']=best_comment[0]
```

其中filter函数中的参数`best_comment`为数据库models.py中定义的变量。

全部代码为：

```python
# blog/views.py
# 第二个参数page_num是通过URL中识别传递过来
def details_view(request,page_num):
    if request.method == 'GET':
        form = CommentForm  #实例化一个CommentForm
    if request.method == 'POST': #提交表单form时都是使用的POST方法
        form = CommentForm(request.POST)   #1:绑定表单:将请求的POST数据装载在CommentForm实例中，只有在绑定了表单才可以验证数据
        # 2.验证表单：验证表单是否通过，如果通过则进行下面操作，表单数据会被存储在字典变量中
        if form.is_valid():
            name = form.cleaned_data['name'] #取出表单中完成验证的数据（字典变量），将字典中key值为name的变量存储在name中
            comment = form.cleaned_data['comment'] #取出表单中完成验证的数据（字典变量），将字典中key值为comment的变量存储在comment中
            c = Comment(name=name,comment=comment) #实例化Comment类，初始化其两个变量
            c.save() #存储到数据库中
            return redirect(to='details_page') #跳转到url.py中name=details_page的URL中

    context = {}
    # comments_set = Comment.objects.all()
    article = Article.objects.get(id=page_num)
    best_comment = Comment.objects.filter(best_comment=True,belong_to=article)
    # 如果存在最优评论，则将其存入字典中
    if best_comment:
        context['best_comment']=best_comment[0]
    # context['comments_set'] = comments_set
    context['form'] = form #将表单填入到上下文
    context['article'] = article

    return render(request,'detail.html',context)
```

在模板中添加最优评论结构：

```html
<!-- blog/detail.html -->
		   <!-- 添加最优评论结构 -->
            {% if best_comment %}
            <div class="ui mini red left ribbon label">
                    <i class="icon fire"></i>
                    BEST
            </div>
            <div class="comment">
                    <div class="avatar">
                        <img src="http://semantic-ui.com/images/avatar/small/matt.jpg" alt="" />
                    </div>
                    <div class="content">
                        <a href="#" class="author"> {{ best_comment.name }} </a>
                        <p class="text" style="font-family: 'Raleway', sans-serif;">
                            {{best_comment.comment}}
                        </p>
                    </div>
            </div>
            <div class="ui divider"></div> 
            {% endif %}
```

![](http://ww1.sinaimg.cn/large/67c0b572gy1fqa0ncm9atj211y0k8aid.jpg)

![](http://ww1.sinaimg.cn/large/67c0b572gy1fqa0nj9odzj211y0k8gtp.jpg)

在提交表单时，需要将数据保存在数据库中，在view中的POST方法中修改数据库保存方法：

```python
c = Comment(name=name,comment=comment) #实例化Comment类，初始化其两个变量
c.save() #存储到数据库中
return redirect(to='details_page') #跳转到url.py中name=details_page的URL中
```

改为：

```python
c = Comment(name=name,comment=comment,belong_to=article) #实例化Comment类，初始化其两个变量
c.save() #存储到数据库中
return redirect(to='details_page',page_num=page_num) #跳转到url.py中name=details_page的URL中
```

- 其中初始化类Comment时，指定类变量belong_to等于article
- redirect时，指定page_num=page_num，表示重定向到当前页，如果设置page_num=3，表示将会跳转到`http://127.0.0.1:8000/details/3`

