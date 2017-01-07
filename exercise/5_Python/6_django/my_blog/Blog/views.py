from django.shortcuts import render
from Blog.models import Article
from Blog.models import Category
from Blog.models import Tag
from django.views.generic import ListView,DetailView
import markdown2

# Create your views here.
class IndexView(ListView):
    """
    首页视图,继承自ListView,用于展示从数据库中获取的文章列表
    """
    template_name = '../templates/index.html'
    # template_name属性用于指定使用哪个模板进行渲染

    context_object_name = 'article_list'
    # context_object_name属性用于给上下文变量取名（在模板中使用该名字）

    def get_queryset(self):
        """
        过滤数据，获取所有已发布文章，并且将内容转成markdown形式
        """
        article_list = Article.objects.filter(status='p')
        # 获取数据库中的所有已发布的文章，即filter(过滤)状态为'p'(已发布)的文章。

        for article in article_list:
            article.body = markdown2.markdown(article.body,)
            # 将markdown标记的文本转为html文本
        return article_list
    def get_context_data(self, **kwargs):
        """
        # 增加额外的数据，这里返回一个文章分类，以字典的形式
        """
        kwargs['category_list']=Category.objects.all().order_by('name')
        return super(IndexView,self).get_context_data(**kwargs)

class ArticleDetailView(DetailView):
    # Django有基于类的视图DetailView,用于显示一个对象的详情页，我们继承它

    model = Article
    # 指定视图获取哪个model

    template_name = "../templates/detail.html"
    # 指定要渲染的模板文件

    context_object_name = "article"
    # 在模板中需要使用的上下文名字

    pk_url_kwarg = 'article_id'
    # 这里注意，pk_url_kwarg用于接收一个来自url中的主键，然后会根据这个主键进行查询
    # 我们之前在urlpatterns已经捕获article_id

    # 指定以上几个属性，已经能够返回一个DetailView视图了，为了让文章以markdown形式展现，我们重写get_object()方法。
    def get_object(self, queryset=None):
        obj = super(ArticleDetailView, self).get_object()
        obj.body = markdown2.markdown(obj.body, extras=['fenced-code-blocks'], )
        return obj

    # # 第五周新增
    # def get_context_data(self, **kwargs):
    #     kwargs['comment_list'] = self.object.blogcomment_set.all()
    #     kwargs['form'] = BlogCommentForm()
    #     return super(ArticleDetailView, self).get_context_data(**kwargs)

class CategoryView(ListView):
    # 继承自ListView,用于展示一个列表

    template_name = "../templates/index.html"
    # 指定需要渲染的模板

    context_object_name = "article_list"
    # 指定模板中需要使用的上下文对象的名字

    def get_queryset(self):
        """
        过滤数据，获取所有已发布文章，并且将内容转成markdown形式
        """
        article_list = Article.objects.filter(category=self.kwargs['cate_id'], status='p')
        # 注意在url里我们捕获了分类的id作为关键字参数（cate_id）传递给了CategoryView，传递的参数在kwargs属性中获取。
        for article in article_list:
            article.body = markdown2.markdown(article.body, extras=['fenced-code-blocks'], )
        return article_list

    # 给视图增加额外的数据
    def get_context_data(self, **kwargs):
        kwargs['category_list'] = Category.objects.all().order_by('name')
        # 增加一个category_list,用于在页面显示所有分类，按照名字排序
        return super(CategoryView, self).get_context_data(**kwargs)

class TagView(ListView):
    template_name = "../templates/index.html"
    context_object_name = "article_list"

    def get_queryset(self):
        article_list = Article.objects.filter(tags=self.kwargs['tag_id'], status='p')
        for article in article_list:
            article.body = markdown2.markdown(article.body, extras=['fenced-code-blocks'], )
        return article_list

    def get_context_data(self, **kwargs):
        kwargs['tag_list'] = Tag.objects.all().order_by('name')
        return super(TagView, self).get_context_data(**kwargs)


class ArchiveView(ListView):
    template_name = "../templates/index.html"
    context_object_name = "article_list"

    def get_queryset(self):
        year = int(self.kwargs['year'])
        month = int(self.kwargs['month'])
        article_list = Article.objects.filter(created_time__year=year, created_time__month=month)
        for article in article_list:
            article.body = markdown2.markdown(article.body, extras=['fenced-code-blocks'], )
        return article_list

    def get_context_data(self, **kwargs):
        kwargs['tag_list'] = Tag.objects.all().order_by('name')
        return super(ArchiveView, self).get_context_data(**kwargs)