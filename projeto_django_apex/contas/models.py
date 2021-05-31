from django.db import models
from django.contrib.auth.models import User


class Conta(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    nome = models.CharField(max_length=255, null=False, blank=False)
    saldo = models.FloatField(default=0)
    data_de_criacao = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'tb_contas'
