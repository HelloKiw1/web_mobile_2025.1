from django.views.generic import View
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout


class Login(View):
    def get(self, request):
        contexto = {'mensagem': ''}
        if request.user.is_authenticated:
            return redirect("/receita")
        else:
            return render(request, 'autenticacao.html', contexto)

    def post(self, request):
        usuario = request.POST.get('usuario', None)
        senha = request.POST.get('senha', None)

        user = authenticate(request, username=usuario, password=senha)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect("/receita/")
            return render(request, 'autenticacao.html', {'mensagem': 'Usuário inativo'})

        return render(request, 'autenticacao.html', {'mensagem': 'Usuário ou Senha Inválidos'})


class Logout(View):
    def get(self, request):
        logout(request)
        return redirect("/")


# ✅ Página Sobre
class Sobre(View):
    def get(self, request):
        return render(request, 'sobre.html')


# ✅ Página Contato
class Contato(View):
    def get(self, request):
        return render(request, 'contato.html')
