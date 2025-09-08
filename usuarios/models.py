
from django.db import models

from django.contrib.auth.models import AbstractUser



class User(AbstractUser):
    choices_tipo_usuario = (('ADMIN', 'ADMINISTRADOR'),
                             ('ATEND', 'ATENDENTE'),
                             ('MEC', 'MECANICO'))

    tipo_usuario = models.CharField(max_length=1, choices=choices_tipo_usuario)
    contato = models.CharField('Contato', max_length=15, blank=True)

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
        ordering = ['last_name']

class UsuarioOrdem(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    #ordem = models.ForeignKey(Empreendimento, on_delete=models.CASCADE)
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.usuario.username}"