from veiculo.models import Veiculo
from django.urls import reverse_lazy
from veiculo.forms import FormularioVeiculo
from django.views.generic import ListView, CreateView

class ListarVeiculos(ListView):

    model = Veiculo
    context_object_name = 'veiculos'
    template_name = 'veiculo/listar.html'

class CriarVeiculos(CreateView):
    
    model = Veiculo
    form_class= FormularioVeiculo
    template_name = 'veiculo/novo.html'
    success_url = reverse_lazy('listar-veiculos')


class EditarVeiculos(ListView):

    model = Veiculo
    context_object_name = 'veiculos'
    template_name = 'veiculo/editar.html'

class DeletarVeiculos(ListView):

    model = Veiculo
    context_object_name = 'veiculos'
    template_name = 'veiculo/deletar.html'

class ExibirVeiculos(ListView):

    model = Veiculo
    context_object_name = 'veiculos'
    template_name = 'veiculo/exibir.html'