from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver


class Perfil(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    data_nascimento = models.DateField(null=True, blank=True)

    class Meta:
        db_table = 'tb_usuarios_perfis'


# post_save é o sinal emitido depois que uma Model é salva
# sender indica qual a model que emitiu esse sinal
@receiver(post_save, sender=User)
def salvar_perfil_de_usuario(sender, instance, created, **kwargs):
    # created indica se User está sendo criado ou salvo. created=True significa novo registro
    if created:
        Perfil.objects.create(usuario=instance)
    else:
        instance.perfil.save()
