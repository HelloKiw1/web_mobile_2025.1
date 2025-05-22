from django.contrib import admin
from django.urls import path, include
from sistema.views import Login, Logout, Sobre, Contato

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Login.as_view(), name='login'),
    path('logout/', Logout.as_view(), name='logout'),
    path('receita/', include('receita.urls'), name='receita'),

    # ✅ Rotas adicionadas
    path('sobre/', Sobre.as_view(), name='sobre'),
    path('contato/', Contato.as_view(), name='contato'),
]
