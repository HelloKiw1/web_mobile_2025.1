from django.views.generic import View
from django.shortcuts import render

class Login(View):

    def get(self, resquest):
        contexto={'mensagem': 'teste 001'}
        return render(resquest, 'autenticacao.html', contexto)