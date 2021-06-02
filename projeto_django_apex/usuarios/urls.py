from django.urls import path
from usuarios import views

app_name = 'usuarios'

urlpatterns = [
    path(
        '',
        views.redireciona_para_perfil,
        name='redireciona_para_perfil'
    ),
    path(
        '<int:id>',
        views.index,
        name='index'
    )
]
