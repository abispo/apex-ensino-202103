from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from contas.models import Conta
from transacoes.models import Transacao


# O decorator @login_required exige que o usuário que acessar essa rota esteja
# autenticado
@login_required
def redireciona_para_perfil(request):
    return redirect(
        reverse('usuarios:index', args=(request.user.id,))
    )


@login_required
def index(request, id):
    if request.user.id != id:
        return redirect(reverse('usuarios:index', args=(request.user.id,)))
    return render(request, 'usuarios/index.html', {})


@login_required
def listar_contas_usuario(request, id):
    if request.user.id != id:
        return redirect(reverse('usuarios:index', args=(request.user.id,)))

    usuario = User.objects.get(pk=request.user.id)
    contas_usuario = usuario.conta_set.all()

    contexto = {
        'contas_usuario': contas_usuario
    }

    return render(
        request,
        'usuarios/listar_contas_usuario.html',
        context=contexto
    )


@login_required
def criar_nova_conta_usuario(request, id):
    if request.user.id != id:
        return redirect(reverse('usuarios:index', args=(request.user.id,)))

    if request.method == 'GET':
        return render(request, 'usuarios/nova_conta_usuario.html', {})

    elif request.method == 'POST':
        usuario = User.objects.get(pk=request.user.id)

        nome_conta = request.POST['nome_conta']
        saldo_inicial_conta = request.POST['saldo_inicial_conta']

        conta = Conta()
        conta.usuario = usuario
        conta.nome = nome_conta

        if saldo_inicial_conta:
            conta.saldo = float(saldo_inicial_conta)

        conta.save()

        return redirect(reverse('usuarios:listar_contas_usuario', args=(request.user.id,)))


@login_required
def listar_transacoes_usuario(request, id):
    if request.user.id != id:
        return redirect(reverse('usuarios:index', args=(request.user.id,)))

    usuario = User.objects.get(pk=request.user.id)
    transacoes_usuario = usuario.transacao_set.all()

    contexto = {
        'transacoes_usuario': transacoes_usuario
    }

    return render(
        request,
        'usuarios/listar_transacoes_usuario.html',
         context=contexto
    )


@login_required
def criar_nova_transacao_usuario(request, id):
    if request.user.id != id:
        return redirect(reverse('usuarios:index', args=(request.user.id,)))

    usuario = User.objects.get(pk=request.user.id)

    if request.method == 'GET':
        contas_usuario = usuario.conta_set.all()

        contexto = {
            'contas_usuario': contas_usuario
        }

        return render(
            request,
            'usuarios/nova_transacao_usuario.html',
            context=contexto
        )

    elif request.method == 'POST':
        conta_debito = Conta.objects.get(
            pk=int(request.POST['conta_debito'])
        )
        conta_credito = Conta.objects.get(
            pk=int(request.POST['conta_credito'])
        )

        valor_transacao = float(request.POST['valor_transacao'])

        transacao = Transacao()
        transacao.conta_debito = conta_debito
        transacao.conta_credito = conta_credito
        transacao.valor = valor_transacao
        transacao.usuario = usuario

        transacao.save()

        conta_debito.saldo -= valor_transacao
        conta_credito.saldo += valor_transacao

        conta_debito.save()
        conta_credito.save()

        return redirect(reverse('usuarios:listar_transacoes_usuario', args=(request.user.id,)))
