from django.conf.urls import url

from . import views

# add namespace for the app,加命名空间予以区分
app_name = 'blog'

urlpatterns = [
    url(r'^$',views.IndexView.as_view(),name='index'),
    url(r'^article/(?P<article_id_view>\d+)$',views.ArticleDetailView.as_view(),name='detail_template'),
    # 使用(?P<>\d+)的形式捕获值给<>中得参数，比如(?P<article_id>\d+)，当访问/blog/article/3时，
    # 将会将3捕获给article_id,这个值会传到views.ArticleDetailView,这样我们就可以判断展示哪个Article了
]