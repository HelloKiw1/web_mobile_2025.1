from django.forms import ModelForm
from veiculo.models import Veiculo

class FormularioVeiculo(ModelForm):

    class Meta:
        model = Veiculo
        exclude = []