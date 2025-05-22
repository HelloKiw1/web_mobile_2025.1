from django.db import models
from datetime import datetime
from veiculo.consts import *

class Veiculo(models.Model):
    marca = models.SmallIntegerField(choices=OPCOES_MARCAS)
    combustivel = models.SmallIntegerField(choices=OPCOES_COMBUSTIVEL)
    cor = models.SmallIntegerField(choices=OPCOES_CORES)

    modelo = models.CharField(max_length=100)
    ano = models. IntegerField()

    preco = models.CharField(max_length=100, null=True)


    foto = models.ImageField(blank=True, null=True, upload_to='veiculo/fotos')


    @property
    def veiculo_novo(self):
        return self.ano == datetime.now().year

    def anos_de_uso(self):
        return datetime.now().year - self.ano
    
    