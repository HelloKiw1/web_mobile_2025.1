from receita.models import Receita
from django.urls import reverse_lazy
from receita.forms import FormularioReceita
from django.views import View
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import FileResponse, Http404
from django.core.exceptions import ObjectDoesNotExist

from rest_framework.generics import ListAPIView
from receita.serializers import SerializadorReceita
from rest_framework.authentication import TokenAuthentication
from rest_framework import permissions


# ✅ Listar receitas (limitado ou para página inicial)
class ListarReceitas(LoginRequiredMixin, ListView):
    model = Receita
    context_object_name = 'receitas'
    template_name = 'receita/listar.html'



# ✅ Criar receita
class CriarReceita(LoginRequiredMixin, CreateView):
    model = Receita
    form_class = FormularioReceita
    template_name = 'receita/novo.html'
    success_url = reverse_lazy('listar-receita')


# ✅ Editar receita
class EditarReceita(LoginRequiredMixin, UpdateView):
    model = Receita
    form_class = FormularioReceita
    template_name = 'receita/editar.html'
    success_url = reverse_lazy('listar-receita')


# ✅ Deletar receita
class DeletarReceita(LoginRequiredMixin, DeleteView):
    model = Receita
    template_name = 'receita/deletar.html'
    success_url = reverse_lazy('listar-receita')


# ✅ Exibir todas as receitas (sem limite)
class ExibirReceitas(ListView):
    model = Receita
    context_object_name = 'receitas'
    template_name = 'receita/exibir.html'


# ✅ Ver detalhes de uma receita
class DetalharReceita(DetailView):
    model = Receita
    template_name = 'receita/detalhes.html'


# ✅ Visualizar foto da receita diretamente
class FotoReceita(View):
    def get(self, request, arquivo):
        try:
            receita = Receita.objects.get(foto='receita/fotos/{}'.format(arquivo))
            return FileResponse(receita.foto)
        except ObjectDoesNotExist:
            raise Http404('Foto não encontrada ou acesso não autorizado!')
        except Exception as exception:
            raise exception

class APIListarReceitas(ListAPIView):
    serializer_class = SerializadorReceita
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Receita.objects.all()