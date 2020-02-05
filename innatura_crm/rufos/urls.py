from django.urls import path

from . import views

urlpatterns = [
    #Ex. /rufos/
    path('', views.index, name='index'),
    #Ex. /rufos/3/
    path('<int:cliente_id>/', views.detalhes_cliente, name='detalhes_cliente'),
    #Ex. /rufos/3/pedidos/
    path('<int:cliente_id>/pedidos/', views.pedidos_cliente, name='pedidos_cliente')
]