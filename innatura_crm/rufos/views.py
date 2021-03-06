from django.shortcuts import render, get_object_or_404

# Create your views here.

from django.http import HttpResponse
from .models import Cliente, Pedido, PedidoProduto, Produto, Entrega


def index(request):
    #return HttpResponse("Aqui o rufos vai colocar todo o front end (Criar uma API)")
    all_clients = Cliente.objects.all()
    context = {
        'all_clients': all_clients,
    }
    return render(request, 'rufos/index.html', context)

def detalhes_cliente(request, cliente_id):
    cliente = get_object_or_404(Cliente, pk=cliente_id)
    pedido = Pedido.objects.filter(pedido_cliente=cliente_id)
    produtos = PedidoProduto.objects.all()
    dias = cliente.cliente_dias_entrega.all()
    context={
        'cliente':cliente,
        'pedido':pedido,
        'produtos':produtos,
        'dias':dias,
    }
    return render(request, 'rufos/detalhes_cliente.html', context)

def detalhes_pedido(request, pedido_id):
    pedido = get_object_or_404(Pedido, pk=pedido_id)
    produto = PedidoProduto.objects.filter(pedido_id=pedido_id)
    context={
        'pedido':pedido,
        'produto':produto,
    }
    return render(request, 'rufos/detalhes_pedido.html', context)

def detalhes_produto(request, produto_id):
    produto = get_object_or_404(Produto, pk=produto_id)
    context={
        'produto':produto,
    }
    return render(request, 'rufos/detalhes_produto.html', context)