from django.forms import ModelForm
from receita.models import Receita

class FormularioReceita(ModelForm):

    class Meta:
        model = Receita
        exclude = []