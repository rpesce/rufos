from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from .models import Cliente


def index(request):
    #return HttpResponse("Aqui o rufos vai colocar todo o front end (Criar uma API)")
    all_clients = Cliente.objects.all()
    output = ', '.join([q.cliente_nome_fantasia for q in all_clients])
    return HttpResponse(output)

def detalhes_cliente(request, cliente_id):
    return HttpResponse("Você está olhando o cliente número: %s." % cliente_id)

def pedidos_cliente(request, cliente_id):
    response = "Você está olhando os pedidos do cliente número: %s."
    return HttpResponse(response % cliente_id)