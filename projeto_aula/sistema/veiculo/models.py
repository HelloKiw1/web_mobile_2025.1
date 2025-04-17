from django.db import models
from datetime import datetime
from veiculo.consts import *

class Veiculo(models.Model):
    marca = models.SmallIntegerField(choices=OPCOES_MARCAS)
    combustivel = models.SmallIntegerField(choices=OPCOES_COMBUSTIVEL)
    cor = models.SmallIntegerField(choices=OPCOES_CORES)

    modelo = models.CharField(max_length=100)
    ano = models. IntegerField()