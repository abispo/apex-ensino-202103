from django.db import models
from contas.models import Conta


class Transacao(models.Model):
    conta_debito = models.ForeignKey(Conta, related_name="conta_debito", on_delete=models.CASCADE)
    conta_credito = models.ForeignKey(Conta, related_name="conta_credito", on_delete=models.CASCADE)
    valor = models.FloatField(null=False, blank=False)
    data_de_criacao = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'tb_transacoes'
