from django.views.generic import View
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.conf import settings

from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response
from rest_framework.authtoken.models import Token

class Login(View):

    def get(self, request):
        contexto={'mensagem': ''}
        if request.user.is_authenticated:
            return redirect("/veiculo")
        else:
            return render(request, 'autenticacao.html', contexto)   

    def post(self, request):
        
        #Obtem as crendenciais de autenticação do formulário
        usuario = request.POST.get('usuario', None)
        senha = request.POST.get('senha', None)

        #Verificar as crendencias de autenticação fornecidas
        user = authenticate(request, username=usuario, password=senha)
        if user is not None:

        #Verificar se o usuario esta ativo
            if user.is_active:
                login(request, user)
                return redirect("/veiculo")

            return render(request, 'autenticacao.html', {'mensagem': ' Usuario inatico'})
    
        return render(request, 'autenticacao.html', {'mensagem': 'Usuario ou Senha Invalidos'})

class Logout(View):
    """
    Class Based View para realizar logout de usuarios.
    """
    def get(self, request):
        logout(request)
        return redirect("/")
    
class LoginAPI(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(
            data=request.data,
            context={
                'request': request
            }
        )
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'id': user.id,
            'nome': user.first_name,
            'email': user.email,
            'token': token.key
        })