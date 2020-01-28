from django.contrib import admin

# Register your models here.
from .models import Cliente, Produto, Pedido, PedidoProduto

class PedidoProdutoInline(admin.StackedInline):
    model = PedidoProduto
    extra = 2

class PedidoAdmin(admin.ModelAdmin):
    list_display = ['id', 'pedido_date', 'pedido_cliente', 'pedido_pagamento', 'pedido_status']
    inlines = [
        PedidoProdutoInline,
    ]
admin.site.register(Pedido, PedidoAdmin)

class ClienteAdmin(admin.ModelAdmin):
    list_display = ['id', 'cliente_nome_fantasia', 'cliente_nome_contato', 'cliente_email', 'cliente_telefone', 'cliente_ativo']
admin.site.register(Cliente, ClienteAdmin)

class ProdutoAdmin(admin.ModelAdmin):
    list_display = ['id', 'produto_nome', 'produto_codigo', 'produto_origem', 'produto_preco_tb1', 'produto_preco_tb2', 'produto_preco_tb3', 'produto_ativo']
admin.site.register(Produto, ProdutoAdmin)