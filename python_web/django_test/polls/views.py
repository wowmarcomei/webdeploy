from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,Http404,HttpResponseRedirect
from polls.models import Question, Choice, Publisher
from django.urls import reverse
from django.views import generic
from django.views.generic import TemplateView,ListView

from .models import Question, Choice

# Create your views here.
# def index(request):
    # 获取Question对象后进行排序：按照时间倒叙，且只获取前5个
    # latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # context = {}
    # context['latest_question_list'] = latest_question_list

    # return render(request, 'polls/index.html', context)

# question_id从URL的参数中传递过来
# def detail(request,question_id):
#     try:
#         question = Question.objects.get(pk=question_id)
#     except Question.DoesNotExist:
#         raise Http404("Question does not exist")
#     return render(request, 'polls/detail.html', {'question': question})


# question_id从URL的参数中传递过来
def vote(request,question_id):
    # return HttpResponse("You're voting on question %s" % question_id)
    question = get_object_or_404(Question,pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # 每次POST一个数据之后都应该使用重定向函数HttpResponseRedirect
        # 它里面接收一个参数URL，利用reverse函数可以避免在视图函数中硬编码HardCode
        # reverse函数只需要传递view函数与软参即可，下面的reverse函数将会返回类似于以下值：
        # '/polls/3/results/',其中3是question.id的值，会被回传到results中
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

# question_id从URL的参数中传递过来
# def results(request,question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     # response = "You're looking at the results of question %s."
#     # return HttpResponse(response % question_id)
#     return render(request, 'polls/results.html', {'question': question})


# 下面使用GenericView
class IndexView(generic.ListView):
    '''
    下面的属性与方法均为继承父类ListView
    '''
    # 表示这个view将会使用哪个模板渲染
    template_name = 'polls/index.html'
    # 标识模板中使用的上下文context对象为：latest_question_list会被传入html模板中引用
    # 而context对象本身则从下面的方法get_queryset中获取
    context_object_name = 'latest_question_list'

    # 重写get_queryset函数，返回值为QuerySet,对应为上面的context_object_name
    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]

    # 上面的写法完全等同于下面四句
    # latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # context = {}
    # context['latest_question_list'] = latest_question_list
    # return render(request, 'polls/index.html', context)

class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

# def detail(request,question_id):
#     try:
#         question = Question.objects.get(pk=question_id)
#     except Question.DoesNotExist:
#         raise Http404("Question does not exist")
#     return render(request, 'polls/detail.html', {'question': question})

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

class AboutView(generic.TemplateView):
    template_name = 'polls/about.html'

class PublisherView(ListView):
    model = Publisher
    template_name = 'polls/about.html'