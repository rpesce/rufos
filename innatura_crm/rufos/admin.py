from django.contrib import admin

# Register your models here.
from .models import Cliente, Produto, Pedido

class PedidoInline(admin.StackedInline):
    model = Pedido
    extra = 2

class ProdutoAdmin(admin.ModelAdmin):
    inlines = [
        PedidoInline,
    ]

admin.site.register(Cliente)
admin.site.register(Produto, ProdutoAdmin)
admin.site.register(Pedido)