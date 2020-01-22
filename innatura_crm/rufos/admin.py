from django.contrib import admin

# Register your models here.
from .models import Person, Cliente

admin.site.register(Person)
admin.site.register(Cliente)