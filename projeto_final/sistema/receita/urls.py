from django.urls import path
from receita.views import *

urlpatterns = [
    path('', ListarReceitas.as_view(), name='listar-receita'),  # /receita/
    path('novo/', CriarReceita.as_view(), name='criar-receita'),  # /receita/novo/
    path('editar/<int:pk>/', EditarReceita.as_view(), name='editar-receita'),  # /receita/editar/1/
    path('deletar/<int:pk>/', DeletarReceita.as_view(), name='deletar-receita'),  # /receita/deletar/1/
    path('exibir/', ExibirReceitas.as_view(), name='exibir-receitas'),  # /receita/exibir/
    path('<int:pk>/detalhes/', DetalharReceita.as_view(), name='detalhar-receita'),  # /receita/1/detalhes/
    path('foto/<str:arquivo>/', FotoReceita.as_view(), name='foto-receita'),  # /receita/foto/nome_arquivo.jpg
    path('api/', APIListarReceitas.as_view(), name='api-listar-receitas'),

]
