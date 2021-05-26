from django.urls import path
from . import views

urlpatterns = [
    # O primeiro argumento é a rota que será associada a view.
    # O segundo argumento é a view que será chamada quando a rota
    # for acessada
    # O terceiro argumento é o nome da rota. Esse nome deve ser único
    # no módulo urls.py

    # /polls
    path('', views.index, name='index'),

    # /polls/5
    path('<int:question_id>/', views.detail, name='detail'),

    # /polls/5/results
    path('<int:question_id>/results/', views.results, name='results'),

    # /polls/5/vote
    path('<int:question_id>/vote/', views.vote, name='vote')
]
