from django.urls import path
from .views import *

urlpatterns = [
    path('registrar_usuario', registrar_usuario, name='registrar_usuario'),
    path('mostrar_resultado', recuperar_registro, name='mostrar_resultado'),
    path('login', login, name='login'),
    path('client_profile', client_profile, name='client_profile'),
    path('add_pet', add_pet, name='add_peth'),
    
]