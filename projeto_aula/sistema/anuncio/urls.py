from django.urls import path
from anuncio.views import *

urlpatterns = [
    path('listar/', ListarAnuncio.as_view(), name='listar-veiculos'), 
    ]