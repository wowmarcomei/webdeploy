from django.urls import path

from . import views

# 给APP增加一个命名空间namespace，这样在模板中就可以使用命名空间如： <a href="{% url 'polls:detail' question.id %}">
app_name='polls'

# urlpatterns = [
#     # ex: /polls/
#     path('', views.index, name='index'),
#     # ex: /polls/5/
#     # 尖括号里的参数将会被捕获到传给后面views中的函数detail
#     # 该参数question_id，必须与views.details中的参数名完全一致
#     path('<int:question_id>/', views.detail, name='detail'),
#     # ex: /polls/5/results/
#     path('<int:question_id>/results/', views.results, name='results'),
#     # ex: /polls/5/vote/
#     path('<int:question_id>/vote/', views.vote, name='vote'),
# ]

# 下面使用GenericView
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
    path('about/', views.AboutView.as_view(),name = 'about'),
    path('abc/', views.PublisherView.as_view()),
]