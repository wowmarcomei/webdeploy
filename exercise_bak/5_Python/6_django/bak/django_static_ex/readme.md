### 使用django加载一个静态网页的方法总结

1. 使用pythons manage.py startapp django_web创建一个新的django的app

2. template为可视化网页模板，views.py负责结构化处理与请求响应处理，modules.py是数据库的代理主要负责数据库的操作

3. 创建了一个django应用以后在settings.py下面需要添加以下语句来添加命令行创建的app:django_web,当然如果使用pycharm自动生成了则无需重复添加

   ```python
   INSTALLED_APPS = [
   	'...',
   	'django_web', #new created app
   ]
   ```

4. 在template下面加入html静态文件

5. 在views.py下定义调用template的视图函数index,

   ```python
   def index(request):
   	return render(request,'index.html') #调配template下面的index.html
   ```

6. 在urls.py下给页面分片一个url.

   ```python
   from django_web.views import index #从新加的app视图层中引入index函数
   urlpatterns = [
     url(r'^admin/',admin.site.urls),
     url(r'^index/',index)  #新加该链接
   ]
   ```

7. 将static目录放在顶层目录下，copy css与image文件

8. 修改index.html文件，首先修改的地方：

   - {% load static %} 默认获取static路径
   - 将路径相关的都换成 {% static %}

9. 在setting.py下面添加目录

   ```
   STATICFILES_DIRS = (os.path.join(BASE_DIR, "static"),)
   ```

最后使用python命令启动服务器:
`python3 manage.py runserver`