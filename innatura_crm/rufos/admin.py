from django.contrib import admin

# Register your models here.
from .models import Cliente, Produto, Pedido

admin.site.register(Cliente)
admin.site.register(Produto)
admin.site.register(Pedido)