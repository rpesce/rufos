from django.shortcuts import render, get_object_or_404

# Create your views here.

from django.http import HttpResponse
from .models import Cliente, Pedido, PedidoProduto


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
    pedidoproduto = PedidoProduto.objects.all().select_related()
    context={
        'cliente':cliente,
        'pedido':pedido,
        'pedidoproduto': pedidoproduto,
    }

    return render(request, 'rufos/detalhes_cliente.html', context)

    #def produtos(pedido):
        #for p in pedido:
            #produto = p.pedidoproduto_set.all()
            #return produto

    #produto = pedido.pedidoproduto_set.all()
    #def produto(pedido_id):
        #produto = PedidoProduto.objects.all().filter(pedido=pedido_id)
    


def pedidos_cliente(request, cliente_id):
    response = "Você está olhando os pedidos do cliente número: %s."
    return HttpResponse(response % cliente_id)