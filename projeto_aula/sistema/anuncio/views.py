from django.shortcuts import render

# Create your views here.
from anuncio.models import Anuncio
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin



class ListarAnuncio(LoginRequiredMixin, ListView):

    model = Anuncio
    context_object_name = 'anuncios'
    template_name = 'anuncio/listar.html'