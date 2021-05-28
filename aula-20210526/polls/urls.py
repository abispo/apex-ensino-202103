from django.urls import path
from . import views

app_name = 'polls'

urlpatterns = [
    # O primeiro argumento é a rota que será associada a view.
    # O segundo argumento é a view que será chamada quando a rota
    # for acessada
    # O terceiro argumento é o nome da rota. Esse nome deve ser único
    # no módulo urls.py

    # /polls
    path('', views.IndexView.as_view(), name='index'),

    # /polls/5
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),

    # /polls/5/results
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),

    # /polls/5/vote
    path('<int:question_id>/vote/', views.vote, name='vote')
]
