### 注册与登陆

#### 1. 引入鉴权与登陆模块authenticate,login

```python
#website/views.py
from django.contrib.auth import authenticate,login
```

#### 2.构造表单获取用户名与密码, 将获取的用户名与密码放入authentication中校验，对比数据库数据,如果数据库中存在数据则进行注册，django将会发送response给浏览器

```python
#website/form.py

# 构造登陆表单
from django import forms

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()
    
```

然后在视图中通过GET方法进行渲染，通过POST方法将数据取出来。

```python
#website/views.py

# 引入登陆用的表单
from website.form import LoginForm

def index_login(request):
    # 定义模板字典
    context = {}
    if request.method == 'GET':
        # 构造并渲染表单
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
```

#### 3.在template中添加表单

```django
<!-- register_login.html  -->

<form class="ui form error" method="post">

    {% if form.errors %}
        <div class="ui error message">
            {{ form.errors }}
        </div>

        {% for field in form  %}
            <div class="{{ field.errors|yesno:'error, ' }} field">
                {{ field.label }}
                {{ field }}
            </div>
        {% endfor %}

    {% else %}
        {% for field in form  %}
            <div class="field">
                {{ field.label }}
                {{ field }}
            </div>
        {% endfor %}

    {% endif %}

    {% csrf_token %}

    <button class="ui inverted red circular right floated button" type="submit">Done</button>
</form>
```

#### 4.在url中加入网址索引

```python
#urls.py

from website.views import listing, index_login

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', listing, name='list'),
    url(r'^list/$', listing, name='list'),
    url(r'^list/(?P<cate>[A-Za-z]+)$', listing, name='list'),
    url(r'^login$', index_login, name='login'),  #添加login
]
```

#### 5.在登陆后的页面template中加入判断用户身份逻辑

> 注：可以从request请求中获取到user对象

```django
<div class="right menu">
    <!-- 获取request中的user对象，判断其是否经过验证 -->
    {% if request.user.is_authenticated %}
        <div class="item">
            <h5 class="ui inverted header">
                <span style="margin-right:20px;">{{ request.user.username }}</span>
                <div class="ui mini circular image">
                    <img src="http://semantic-ui.com/images/avatar/small/matt.jpg" />
                </div>
            </h5>
        </div>
        <div class="item">
            <a href="#" class="ui inverted circular button">Logout</a>
        </div>
    {% else %}
        <div class="item">
            <h5 class="ui inverted header">
                <span style="margin-right:20px;">{{ request.user.username }}</span>
                <div class="ui mini circular image">
                    <img src="http://semantic-ui.com/images/avatar/small/matt.jpg"/>
                </div>
            </h5>
        </div>
        <div class="item">
            <a href="#" class="ui inverted circular button">Signup/Login</a>
        </div> 
    {% endif %}
        
</div>
```

#### 6.引入用户模型User

> 为了使用户使用不同的profile，我们在数据库中引入User

```python
#models.py

# 引入用户模型
from django.contrib.auth.models import User

class UserProfile(models.Model):
    belong_to = models.OneToOneField(to=User, related_name='profile')
    profile_image = models.FileField(upload_to='profile_image')
```

在模板文件中修改用户头像逻辑：

```html
<!-- template/listing.html -->

<div class="ui mini circular image">
    <!-- 如果请求的用户在数据库中存在profile_image的话则显示该图片，否则显示默认图片 -->
    {% if request.user.profile.profile_image %}
        <img src="/upload/{{ request.user.profile.profile_image }}"/>
    {% else %}
        <img src="http://semantic-ui.com/images/avatar/small/matt.jpg"/>
    {% endif %}                                
</div>
```

#### 7.完善登陆与注册逻辑

前面使用的是自定义的form进行注册，其实Django有自带的功能强大的表单可供注册验证使用。

```python
#website/views.py

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
```

```python
#website/urls.py

from website.views import listing, index_login,index_register

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', listing, name='list'),
    url(r'^list/$', listing, name='list'),
    url(r'^list/(?P<cate>[A-Za-z]+)$', listing, name='list'),
    url(r'^login$', index_login, name='login'),
    url(r'^register/$', index_register, name='register'),
    # logout后面传入一个字典变量，指明了跳转页面是/register这个页面
    url(r'^logout/$', logout, {'next_page': '/register'}, name='logout'),
]
```

![](https://github.com/wowmarcomei/workstation/blob/master/python_web/level2/11_register_and_login/ex1.png)

![](https://github.com/wowmarcomei/workstation/blob/master/python_web/level2/11_register_and_login/ex2.png)