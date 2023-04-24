from django.shortcuts import render
from django.http import HttpResponse, Http404, JsonResponse
from .models import Question
from .serializers import QuestionSerializer
from rest_framework import generics

# Create your views here.
def index(request):
    questions = Question.objects.all()
    questions_list = '<br />'.join([question.question_text for question in questions])
    # return HttpResponse(questions_list)
    return render(request, 'index.html', context={ 'latest_question_list': questions })

def detail(request, question_id):
    try:
      q = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
      raise Http404('Question not found')
    # return HttpResponse(f'You are looking at question #{question_id}: {q.question_text}')
    return render(request, 'detail.html', context={ 'question': q })

def results(request, question_id):
    q = Question.objects.get(pk=question_id)
    return HttpResponse(f'These are the results for question #{question_id}: {q.question_text}')

def vote(request, question_id):
    q = Question.objects.get(pk=question_id)
    return HttpResponse(f'You are voting on question #{question_id}: {q.question_text}')

# def api_test(request):
#     questions = Question.objects.all()
#     return JsonResponse(questions)

class QuestionList(generics.ListCreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer