from django.urls import path
from veiculo.views import *

urlpatterns = [
    path('', ListarVeiculos.as_view(), name='listar-veiculos'),                      # /veiculo/
    path('novo/', CriarVeiculos.as_view(), name='criar-veiculos'),
    path('deletar/<int:pk>', DeletarVeiculos.as_view(), name='deletar-veiculos'),   # /veiculo/deletar/1/
    path('exibir', ExibirVeiculos.as_view(), name='exibir-veiculos'),      # /veiculo/exibir/1/
    path('<int:pk>/', EditarVeiculos.as_view(), name='editar-veiculos'),
    path('<int:pk>/detalhes/', DetalharVeiculo.as_view(), name='detalhar-veiculo'),

]