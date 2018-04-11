第一步：渲染表单，使用form类

第二步：绑定表单，在view层进行校验

第三步：返回校验结果



### 1.准备工作，在models中创建一个评论模型数据库

评论有name与评论内容。

```python
class Comment(models.Model):
    name = models.CharField(null=True,blank=True, max_length=50)
    comment = models.TextField()
    def __str__(self):
        return self.comment
```

### 2.在view层创建视图模型, 将表单form传递到模板进行渲染

新建form.py文件

```python
# 继承forms类来创建表单
from django import forms

# 创建的CommentForm类被实例化后，一旦被template层引用，django将会自动被创建表单
class CommentForm(forms.Form):
    name = forms.CharField(max_length=50)
    comments = forms.CharField()
```

在view层进行传递:

```python
def details(request):
    context = {}
    comments_set = Comment.objects.all()
    context['comments_set'] = comments_set

    form = CommentForm #实例化表单
    context['form'] = form #将表单填入到上下文

    return render(request,'detail.html',context)
```

在Template模板`details.html`中进行渲染:

```html
		<!-- 1:显示历史评论comment -->
            <div class="ui comments">
                {% for comment in comments_set %}
                    <div class="comment">
                        <div class="avatar">
                          <img src="http://semantic-ui.com/images/avatar/small/matt.jpg"/>
                        </div>
                        <div class="content">
                            <a href="#" class="author"> {{ comment.name }} </a>
                            <div class="metadata">
                                <div class="date">2 days ago</div>
                            </div>
                            <p class="text" style="font-family: 'Raleway', sans-serif;">
                                {{comment.comment}}
                            </p>
                        </div>
                    </div>
                {% endfor %}
            </div>

            <div class="ui divider"></div>

            <!-- 2.通过form提交评论comment到服务器 -->
            <form class="ui tiny form" action="" method="post">  
                <!-- {{ form }}，form.as_p可以将表单加载在p标签中，不加也可以 -->
                {{ form.as_p }}
                <button type="submit" class="ui blue button" >Click</button>
            </form>
```



### 3. 在view层对方法进行分离判断

由于表单是使用`POST`方法，而除了提交表单外，还有正常访问的`GET`请求，所以需要进行判断是`POST`还是`GET`。



```python
def details(request):
    context = {}
    comments_set = Comment.objects.all()
    context['comments_set'] = comments_set

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
            return redirect(to='details') #跳转到url.py中name=details的URL中

    context['form'] = form #将表单填入到上下文

    return render(request,'detail.html',context)
```

![](https://ws1.sinaimg.cn/large/006tNc79ly1fq7c2bxcd6j311g0nt0vm.jpg)



### 4.自定义表单验证器

```python
# 继承forms类来创建表单
from django import forms
from django.core.exceptions import ValidationError

# 自定义一个验证器,传递参数是评论本身,评论必须大于4个字节
def words_validator(comment):
    if len(comment) < 4:
        raise ValidationError('Not enough words')

# 自定义一个验证器,传递参数是评论本身,评论中不能包含某字符
def chars_validator(comment):
    if 'a' in comment:
        raise ValidationError('not allowed to input that word')

# 创建的CommentForm类被实例化后，一旦被template层引用，django将会自动被创建表单
class CommentForm(forms.Form):
    name = forms.CharField(max_length=50)
    # 传递参数widget使得评论框变成大的输入框,传递参数error_messages为django自带验证器，参数validators为自定义验证器
    comment = forms.CharField(
        widget=forms.Textarea(),
        error_messages={
            'required': 'wow,such words'
        },
        validators = [words_validator,chars_validator]
    )
```

> 注意验证器不仅可以用在表单form中，也同样可以用于models中。

在Template中修改form逻辑。

```html
        <!-- 2.通过form提交评论comment到服务器 -->
        <form class="ui error tiny form" action="" method="post">

            <!-- {{ form }}，form.as_p可以将表单加载在p标签中，不加也可以 -->
            <!-- {{ form.as_p }} -->

            <!-- 如果出现错误，那么先显示一个装载了错误信息的div，然后是表单 -->
            {% if form.errors %}
                <!-- 装载错误信息的div -->
                <div class="ui error message">
                    {{ form.errors }}
                </div>
                <!-- 正常表单 -->
                {% for field in form %}
                <div class="{{ field.errors|yesno:'error, '}}  field"> <!-- 使用django的yesno过滤器，只对出错的field渲染错误提醒 -->
                    {{field.label}} 
                    {{field}}
                </div>
                {% endfor %} 
            <!-- 如果没有出现错误，则一切正常，正常渲染表单 -->
            {% else %} 
                {% for field in form %}
                <div class="field">
                    {{field.label}} {{field}}
                </div>
                {% endfor %} 
            {% endif %} 

            {% csrf_token %}
            <!-- 表单中，需要进行防止跨站攻击 -->
            <button type="submit" class="ui blue button">Click</button>
        </form>
```

![](https://github.com/wowmarcomei/workstation/blob/master/python_web/level2/6_myblog_post_form/ex.png)