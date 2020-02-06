from django.urls import path

from . import views

app_name = 'rufos'
urlpatterns = [
    #Ex. /
    path('', views.index, name='index'),
    #Ex. /3/
    path('<int:cliente_id>/', views.detalhes_cliente, name='detalhes_cliente'),
    #Ex. /3/pedidos/
    path('<int:cliente_id>/pedidos/', views.pedidos_cliente, name='pedidos_cliente')
]