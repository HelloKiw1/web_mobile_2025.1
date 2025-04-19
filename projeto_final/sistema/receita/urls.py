from django.urls import path, include
from receita.views import *

urlpatterns = [
    path('', ListarReceitas.as_view(), name='listar-receita')
]