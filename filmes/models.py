from django.db import models
from django.contrib.auth.models import User


class Films(models.Model):
    nome = models.CharField(max_length=50, blank=False)
    ano = models.CharField(max_length=4, blank=False)
    status = models.BooleanField(default=False)
    usuario = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        verbose_name = 'Filme'

    def __str__(self):
        return "{}".format(self.nome)
