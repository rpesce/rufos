from django.shortcuts import render, get_object_or_404

# Create your views here.

from django.http import HttpResponse
from .models import Cliente, Pedido


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
    return render(request, 'rufos/detalhes_cliente.html', {'cliente':cliente, 'pedido':pedido})

def pedidos_cliente(request, cliente_id):
    response = "Você está olhando os pedidos do cliente número: %s."
    return HttpResponse(response % cliente_id)