from django.urls import path, include
from veiculo.views import *

urlpatterns = [
    path('', ListarVeiculos.as_view(), name='listar-veiculos'),
    path('', DeletarVeiculos.as_view(), name='deletar-veiculos'),
    path('', EditarVeiculos.as_view(), name='editar-veiculos'),
    path('', ExibirVeiculos.as_view(), name='exibir-veiculos'),
]