from django.db import models
from datetime import datetime

class Anuncio(models.Model):
    nome = models.CharField(max_length=100)
