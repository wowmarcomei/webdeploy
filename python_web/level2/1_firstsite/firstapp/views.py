# 添加HttpResponse类
from django.shortcuts import render, HttpResponse
# 从app的models中导入People类，从django模板中导入Context(上下文)与Template(模板)
from firstapp.models import People
from django.template import Context, Template

# Create your views here.

# 定义一个函数first_try，传入软参为request(用户发来的请求，暂时不管该参数)
def first_try(request):
    # 创建People类的一个实例化对象man，类初始化的参数即为类的变量
    # 实例化了下面的对象man以后，即是使用了django的M层Models创建了数据表People的一个数据，且对其进行了初始化
    man = People(name='Spork', job='officer') 
    # 创建People的另外一个对象woman
    woman = People(name='Lily', job='Engineer')

    # 使用template将其渲染到我们的网页中，制作如下的模板（实际上是字符串）
    html_string = '''
         <html>
            <head>
                <meta charset="utf-8">
                <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/semantic-ui/2.2.6/semantic.css" media="screen" title="no title">
                <title>firstapp</title>
            </head>

            <body>
                <h1 class="ui center aligned icon header">
                    <i class="hand spock icon"></i>
                    Hello, {{ man.name }}
                    <p>
                        Hi, {{ woman.name }}! How is it going?
                    </p>
                    <p>
                        Are you an {{ woman.job }}?
                    </p>
                </h1>
            </body>
        </html>    
    '''
    # 使用Template类初始化，将字符串html_string变成模板
    t = Template(html_string)
    # 为了将数据库中的数据填充到模板，需要将数据变成上下文，使用Context类将数据表中的数据man变成上下文
    # Context里接收的参数是字典类型数据，
    # 字典数据为 key: value类型，其中value部分即是一个常规变量，下面例子中该变量为People类的对象
    # 应用到模板中即变成了对象man的变量name值。
    # 想象Template就是生活中的一个拼图样板，大括号{{ }}里的东西就是我们需要填入的东西，在Django中这个东西即是上下文Context，Context参数为字典
    c = Context({'man':man, 'woman':woman })
    # 使用render函数，将上下文c填入到模板t中
    web_page = t.render(c)

    # 返回参数为HttpResponse对象
    return HttpResponse(web_page)