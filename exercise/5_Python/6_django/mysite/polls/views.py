from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from .models import Question
from django.template import loader

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
    # 注意: 下面字典变量作为content,传递给html,字典变量的key键值question_mxh作为html的变量被html直接引用
    return render(request,'polls/detail.html',{'question_mxh':question})

def result(request,question_id):
    response = "You're looking at the result of question %s."
    return HttpResponse(response %question_id)
def vote(request,question_id):
    return HttpResponse("You're voting on question %s." %question_id)
