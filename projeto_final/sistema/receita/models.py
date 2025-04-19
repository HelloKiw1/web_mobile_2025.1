from django.db import models
from datetime import datetime
from receita.consts import *

class Receita(models.Model):
    marca = models.SmallIntegerField(choices=OPCOES_TIPO)
    cor = models.SmallIntegerField(choices=OPCOES_GOSTO)

'''    modelo = models.CharField(max_length=100)
    ano = models. IntegerField() '''    
