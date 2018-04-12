### 正则表达式选择网址

1. 顾头式: `^/detail`

   表示的是以`/detail`开头的url，如：

   ```python
   /detail/abc/efg

   /detail123456

   /detail_*&sadh2
   ```

2. 顾尾式：`detail$`

   表示的是以`detail`结尾的url，如：

   ```python
   abc/efg/detail
   a1231234detail
   _87er&*detail
   ```

3. 精确式：`^detail$`

   表示的是`www.blog.com/detail`

4. 匹配`detail/123`

   - 限定三位数字：`/detail/(\d){3}`
   - 限定多位数字：`/detail/(\d+)`

```python
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^home/', home, name=None),
    url(r'^details/(?P<page_num>\d+)$', details, name='details'), 
]
```

关于`url(r'^details/(?P<page_num>\d+)$', details, name='details')`的解读：`(?P)`表示的是括号里的是正则表达式，尖括号里的是变量，`\d+`匹配出来的值将会被存储在`page_num`中，`name='details'`里的details可以抽象理解为url的名字，唯一代表这个url，相当于给这个网址取的名字就叫做details，一般用于template里作为变量（也有用于view和model中）。在Template中使用时，可以按照如下方式进行：

```html
<a href="{% url 'details' article.id %}">
```

即使用django的url标签来进行，其中`'details'`就是从上面URL.py中的urlpatterns中读取到的`name='details'`，两者名字保持一致即可; 其中`article.id`是`name='details'`的参数，即网址的参数`page_num`。

其实在template中使用url标签的方法为：

```html
1.不带参数的：
{% url 'name' %}

2.带参数的：参数可以是变量名
{% url 'name' 参数 %}

'name'指的就是urlpatterns中唯一代表url的名字变量
```

5. 完整示例

当遇到urlpatterns的地址包含有参数的时候，如：

`(r'^(?P<year>\d{4})/(?P<month>\d{1,2})/$','news_list' )`

有两个参数`year`与`month`，最终的地址如归档的地址<http://www.mysite.com/2010/02>,会被传递到view中的news_list方法中处理。

- 1) 可以将url.py中修改urlpatterns，给url添加一个名字，使用该名字就可以在Template中引用：

```python
# mysite/urls.py
urlpatterns = [
    url(r'^(?P<year>\d{4})/(?P<month>\d{1,2})/$',news_list,name="news_archive" ),
]
```

其中正则表达式中两个括号中的参数为`year`和`month`，`news_list`为view.py定义的试图函数，`news_archive`为url的名字，使用该名字就表示引用该url。



- 2) 在template中使用url标签：

```html
<a href="{%url 'news_archive' 2010  02%}">2010年02月</a> 
或者这样:
<a href="{%url 'news_archive' year=2010  month=02%}">2010年02月</a> 
```

其中`new_archive`为urlpatterns定义的url，后面的参数2010与02传递会urlpatterns中定义的`year`和`month`.



- 3) 在views.py中定义函数news_list,也必须带上参数`year`和`month`

```python
def news_list(request,year,month):
    print 'year:',year
    print 'monty:',month
    ......
```

  

