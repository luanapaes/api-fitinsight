from django.urls import path
from app_cad_user import views

urlpatterns = [
   # rota, view responsável, nome de referência
   #ex: usuario.com
   path('', views.home,name='home'),

   #usuario.com/usuarios
   path('usuarios/', views.usuario, name='usuarios')

]
