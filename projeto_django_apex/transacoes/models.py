from django.db import models
from django.contrib.auth.models import User
from contas.models import Conta


class Transacao(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    conta_debito = models.ForeignKey(
        Conta, related_name="conta_debito",
        on_delete=models.SET_NULL,
        null=True
    )
    conta_credito = models.ForeignKey(
        Conta,
        related_name="conta_credito",
        on_delete=models.SET_NULL,
        null=True
    )
    valor = models.FloatField(null=False, blank=False)
    data_de_criacao = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'tb_transacoes'
