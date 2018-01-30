from django.contrib import admin
from .models import Cliente
# Register your models here.

class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nome','cpf','sexo','telefone','instagran')
    icon = '<i class="material-icons">people_outline</i>'



admin.site.register(Cliente,ClienteAdmin)
