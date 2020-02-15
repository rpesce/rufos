from django.urls import path

from . import views

app_name = 'rufos'
urlpatterns = [
    #Ex. /
    path('', views.index, name='index'),
    #Ex. /3/
    path('<int:cliente_id>/', views.detalhes_cliente, name='detalhes_cliente'),
    #Ex. pedidos/3/
    path('pedidos/<int:pedido_id>/', views.detalhes_pedido, name='detalhes_pedido')
]