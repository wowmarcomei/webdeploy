from django.shortcuts import render
from blog.models import Article
from blog.models import Category
from django.views.generic import ListView,DetailView,ArchiveIndexView
import markdown2

# Create your views here.

class IndexView(ListView):
    """
    首页视图,继承自Listview,用于展示从数据库中获取的文章列表
    """
    template_name = 'blog/index.html'
    # 重置属性template_name,用于指定使用哪个模板进行渲染

    context_object_name = 'article_list'
    # 重置属性context_object_name,用于给上下文变量取名(在模板中使用该名字)

    def get_queryset(self):
        """
        过滤数据,获取所有已发布文章,并且将内容转换为markdown形式
        """
        article_list = Article.objects.filter(status='p')

        for article in article_list:
            article.body = markdown2.markdown(article.body,)
            #将markdown标记的文本转换为html文本
        return article_list

    def get_context_data(self, **kwargs):
        """
        增加额外的数据,这里返回一个文章分类,以字典的形式
        """
        kwargs['category_list'] = Category.objects.all().order_by('name')
        return super(IndexView,self).get_context_data(**kwargs)

class ArticleDetailView(DetailView):
    model = Article
    # 指定视图获取哪个model

    template_name = 'blog/details.html'
    # 指定要渲染的模板文件

    context_object_name = 'article_view'
    # 在模板中需要使用的上下文名字, 即模板子中的变量

    pk_url_kwarg = 'article_id_view'
    #这里注意,pk_url_kwarg用于接收一个来自url中的主键，然后会根据这个主键进行查询
    #我们已经在blog/urls.py中定义了捕获article_id_view传递进来,

    def get_object(self, queryset=None):
        """
        返回该视图要显示的对象
        :param queryset:
        :return:
        """
        obj = super(ArticleDetailView,self).get_object()
        obj.body = markdown2.markdown(obj.body,extras=['fenced-code-blocks'],)
        return obj


