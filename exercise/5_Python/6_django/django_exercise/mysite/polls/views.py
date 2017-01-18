from django.shortcuts import render, get_object_or_404,reverse
from django.http import HttpResponse, Http404,HttpResponseRedirect
from .models import Question,Choice
from django.template import loader
from django.views import generic

# Create your views here.
def index(request):
    # Test1: return a simple answer
    # return HttpResponse("hello, wolrd. You're at the polls index.")
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # output = ', '.join([q.question_text for q in latest_question_list])
    # return HttpResponse(output)
    # template = loader.get_template('polls/index.html')
    context={
        'latest_question_list': latest_question_list,
    }
    # return HttpResponse(template.render(context,request))
    return render(request,'polls/index.html',context)

def detail(request,question_id):
    # Test1
    # return HttpResponse("You're looking at question %s." %question_id)
    # Test2
    # try:
    #     question =Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404("Question does not exsit")
    # Test3
    question = get_object_or_404(Question,pk=question_id)
    # 注意: 下面字典变量作为content,传递给html,字典变量的key键值question作为html的变量被html直接引用
    return render(request,'polls/detail.html',{'question':question})

def result(request,question_id):
    # response = "You're looking at the result of question %s."
    # return HttpResponse(response %question_id)
    question = get_object_or_404(Question,pk=question_id)
    return render(request,'polls/result.html',{'question':question})

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
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
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

class IndexView(generic.ListView):
    # 重写类的的两个属性值
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'
    # for ListView, the automatically generated context variable is question_list.
    # To override this we provide the context_object_name attribute,
    # specifying that we want to use latest_question_list instead.As an alternative approach,
    # you could change your templates to match the new default context variables –
    # but it’s a lot easier to just tell Django to use the variable you want.

    def get_queryset(self):
        """
        重写get_queryset函数,获取最后publish的五个问题
        """
        return Question.objects.order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
    # 重写类的的两个属性值
    model = Question
    # since we are using the Django model(Question),
    # Django is able to determine an appropriate name for the context variable.
    # means  variable is provided automatically in template,
    # no need to add define a variable 'question' for the template

    template_name = 'polls/detail.html'

class ResultView(generic.DetailView):
    # 重写类的的两个属性值
    model = Question
    template_name = 'polls/result.html'