from django.forms import ModelForm
from receita.models import Receita
from django import forms

class FormularioReceita(ModelForm):

    class Meta:
        model = Receita
        exclude = []

    nome = forms.CharField(required=True)  