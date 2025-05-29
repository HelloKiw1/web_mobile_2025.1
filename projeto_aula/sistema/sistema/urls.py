from django.contrib import admin
from django.urls import path, include
from sistema.views import Login, Logout, LoginAPI

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Login.as_view(), name='login'),
    path('autenticacao-api/', LoginAPI.as_view()),
    path('logout/', Logout.as_view(), name='logout'),
    path('veiculo/', include('veiculo.urls'), name='veiculo'),
    path('anuncio/', include('anuncio.urls'), name='anuncio'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

