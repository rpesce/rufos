from django.urls import path

from . import views

app_name = 'rufos'
urlpatterns = [
    #Ex. /
    path('', views.index, name='index'),
    #Ex. clientes/1/
    path('clientes/<int:cliente_id>/', views.detalhes_cliente, name='detalhes_cliente'),
    #Ex. pedidos/1/
    path('pedidos/<int:pedido_id>/', views.detalhes_pedido, name='detalhes_pedido'),
    #Ex. produtos/1/
    path('produtos/<int:produto_id>/', views.detalhes_produto, name='detalhes_produto'),
]