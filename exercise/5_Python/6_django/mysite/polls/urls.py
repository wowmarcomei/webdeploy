from django.conf.urls import url

from . import views

# add namespace for the app,加命名空间予以区分
app_name = 'polls'

urlpatterns = [
	#ex: /polls/
	url(r'^$',views.index, name='index'),
	#ex: /polls/5/
	url(r'^specificssd/sdhj/(?P<question_id>[0-9]+)/$',views.detail,name='detail'),
	#ex: /polls/5/results
	url(r'^(?P<question_id>[0-9]+)/results/$',views.result,name='results'),
	#ex: /polls/5/vote
	url(r'^(?P<question_id>[0-9]+)/vote/$',views.vote,name='vote'),
]
