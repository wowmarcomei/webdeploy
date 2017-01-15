from django.conf.urls import url

from . import views

# add namespace for the app,加命名空间予以区分
app_name = 'blog'

urlpatterns = [
    url(r'^$',views.IndexView.as_view(),name='index'),
    url(r'^article/(?P<article_id_view>\d+)$',views.ArticleDetailView.as_view(),name='detail_template'),
]