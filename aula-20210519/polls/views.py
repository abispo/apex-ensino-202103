from django.http import HttpResponse
from django.shortcuts import render
from .models import Question


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {
        'latest_question_list': latest_question_list
    }
    return render(request, 'polls/index.html', context)


def detail(request, question_id):
    return HttpResponse(f"Você está nos detalhes da pergunta {question_id}")


def results(request, question_id):
    return HttpResponse(f"Você está olhando os resultados da pergunta {question_id}")


def vote(request, question_id):
    return HttpResponse(f"Você está votando na pergunta {question_id}")