
from django.urls import path
from app_cad_user import views

urlpatterns = [
    # rota, view responsável, nome de referencia
    # usuarios.com
    path('', views.home, name='index'),
    #usuarios.com/user
    path('vendas/', views.vendas, name='listagem_vendas'),

]
