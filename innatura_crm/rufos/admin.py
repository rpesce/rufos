from django.contrib import admin

# Register your models here.
from .models import Cliente, Produto

admin.site.register(Cliente)
admin.site.register(Produto)