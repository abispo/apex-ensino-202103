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
    ),
    path(
        '<int:id>/contas',
        views.listar_contas_usuario,
        name='listar_contas_usuario'
    ),
    path(
        '<int:id>/contas/nova',
        views.criar_nova_conta_usuario,
        name='criar_nova_conta_usuario'
    ),

    # Transações
    path(
        '<int:id>/transacoes',
        views.listar_transacoes_usuario,
        name='listar_transacoes_usuario'
    ),
    path(
        '<int:id>/transacoes/nova',
        views.criar_nova_transacao_usuario,
        name='criar_nova_transacao_usuario'
    )
]
