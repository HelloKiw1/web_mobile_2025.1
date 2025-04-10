from django.contrib import admin
from django.urls import path
from sistema.views import Login

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Login.as_view(), name='login')
]
