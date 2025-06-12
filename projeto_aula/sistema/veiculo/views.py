from veiculo.models import Veiculo
from django.urls import reverse_lazy
from veiculo.forms import FormularioVeiculo
from django.views import View
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import FileResponse, Http404
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.generics import ListAPIView, DestroyAPIView
from veiculo.serializers import SerializadorVeiculo
from rest_framework.authentication import TokenAuthentication
from rest_framework import permissions

class ListarVeiculos(LoginRequiredMixin, ListView):
    model = Veiculo
    context_object_name = 'veiculos'
    template_name = 'veiculo/listar.html'


class CriarVeiculos(LoginRequiredMixin, CreateView):
    
    model = Veiculo
    form_class= FormularioVeiculo
    template_name = 'veiculo/novo.html'
    success_url = reverse_lazy('listar-veiculos')


class EditarVeiculos(LoginRequiredMixin, UpdateView):

    model = Veiculo
    form_class = FormularioVeiculo
    template_name = 'veiculo/editar.html'
    success_url = reverse_lazy('listar-veiculos')

class DeletarVeiculos(LoginRequiredMixin, DeleteView):

    model = Veiculo
    template_name = 'veiculo/deletar.html'
    success_url = reverse_lazy('listar-veiculos')


class ExibirVeiculos(ListView):

    model = Veiculo
    context_object_name = 'veiculos'
    template_name = 'veiculo/exibir.html'

class FotoVeiculo(View):
    def get(self, request, arquivo):
        try:
            veiculo = Veiculo.objects.get(foto='veiculo/fotos/{}' .format(arquivo))
            return FileResponse(veiculo.foto)
        except ObjectDoesNotExist:
            raise Http404('Foto não encontrada ou acesso não autorizado!')
        except Exception as exception:
            raise exception

class DetalharVeiculo(DetailView):
    model = Veiculo
    template_name = 'veiculo/detalhes.html'

class APIListarVeiculos(ListAPIView):
    serializer_class = SerializadorVeiculo
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Veiculo.objects.all()
    
class APIDeletarVeiculo(DestroyAPIView):
    serializer_class = SerializadorVeiculo
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Veiculo.objects.all()