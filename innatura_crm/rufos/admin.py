from django.contrib import admin

# Register your models here.
from .models import Cliente, Produto, Pedido, PedidoProduto

class PedidoProdutoInline(admin.StackedInline):
    model = PedidoProduto
    extra = 2

class PedidoAdmin(admin.ModelAdmin):
    inlines = [
        PedidoProdutoInline,
    ]

admin.site.register(Cliente)
admin.site.register(Produto)
admin.site.register(Pedido, PedidoAdmin)
