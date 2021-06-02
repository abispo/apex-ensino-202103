from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required


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
