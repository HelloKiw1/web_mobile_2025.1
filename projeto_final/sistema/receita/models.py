from django.db import models
from datetime import datetime
from receita.consts import *

class Receita(models.Model):
    nome = models.CharField(max_length=100, null=True, blank=True)
    tipo = models.SmallIntegerField(choices=OPCOES_TIPO, null=True, blank=True)
    gosto = models.SmallIntegerField(choices=OPCOES_GOSTO, null=True, blank=True)
    tempo_preparo = models.DurationField(null=True, blank=True)
    porcoes = models.SmallIntegerField(null=True, blank=True)
    dificuldade = models.SmallIntegerField(choices=OPCOES_DIFICULDADE, null=True, blank=True)
    
    ingredientes = models.TextField(max_length=10000, null=True, blank=True)
    receita = models.TextField(max_length=10000, null=True, blank=True)
    foto = models.ImageField(blank=True, null=True, upload_to='receita/fotos')

    def __str__(self):
        return self.nome if self.nome else 'Receita sem nome'
