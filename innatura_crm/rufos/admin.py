from django.contrib import admin

# Register your models here.
from .models import Cliente, Produto, Pedido, PedidoProduto

class PedidoProdutoInline(admin.StackedInline):
    model = PedidoProduto
    extra = 2

class PedidoAdmin(admin.ModelAdmin):
    list_display = ['id', 'pedido_date', 'pedido_cliente', 'pedido_pagamento', 'pedido_sub_total', 'pedido_status']
    readonly_fields=('pedido_sub_total',)
    list_filter = ['pedido_cliente', 'pedido_status']
    ordering = ('id', 'pedido_date', 'pedido_cliente', 'pedido_pagamento', 'pedido_status')
    inlines = [
        PedidoProdutoInline,
    ]
admin.site.register(Pedido, PedidoAdmin)

class ClienteAdmin(admin.ModelAdmin):
    list_display = ['id', 'cliente_nome_fantasia', 'cliente_nome_contato', 'cliente_email', 'cliente_telefone', 'cliente_ativo']
    search_fields = ['cliente_nome_fantasia', 'cliente_nome_contato', 'cliente_email']
    list_filter = ['cliente_nome_fantasia', 'cliente_nome_contato']
    ordering = ('id', 'cliente_nome_fantasia', 'cliente_nome_contato', 'cliente_email', 'cliente_telefone', 'cliente_ativo')
admin.site.register(Cliente, ClienteAdmin)

class ProdutoAdmin(admin.ModelAdmin):
    list_display = ['id', 'produto_nome', 'produto_codigo', 'produto_preco_tb1', 'produto_preco_tb2', 'produto_preco_tb3', 'produto_ativo']
    search_fields = ['produto_nome', 'produto_origem']
    list_filter = ['produto_nome', 'produto_origem']
    ordering = ('id', 'produto_nome', 'produto_codigo', 'produto_preco_tb1', 'produto_preco_tb2', 'produto_preco_tb3', 'produto_ativo')
admin.site.register(Produto, ProdutoAdmin)