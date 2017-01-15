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
    template_name = 'blog/details.html'
    context_object_name = 'article_view' #与模块中的变量保持一致
    pk_url_kwarg = 'article_id_view'  #与url模块中的传递参数一致

    def get_object(self, queryset=None):
        obj = super(ArticleDetailView,self).get_object()
        obj.body = markdown2.markdown(obj.body,extras=['fenced-code-blocks'],)
        return obj


