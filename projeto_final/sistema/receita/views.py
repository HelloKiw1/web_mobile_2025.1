from receita.models import Receita
from django.views.generic import ListView

class ListarReceitas(ListView):

    model = Receita
    context_object_name = 'receitas'
    template_name = 'receita/listar.html'