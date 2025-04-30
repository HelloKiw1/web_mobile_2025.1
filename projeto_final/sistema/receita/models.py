from django.db import models
from datetime import datetime
from receita.consts import *

class Receita(models.Model):
    nome = models.CharField(max_length=100, null=True, blank=True)
    tipo = models.SmallIntegerField(choices=OPCOES_TIPO, null=True, blank=True)
    gosto = models.SmallIntegerField(choices=OPCOES_GOSTO, null=True, blank=True)