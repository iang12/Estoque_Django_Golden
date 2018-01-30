from django.contrib import admin
from .models import Ordem_Servico
# Register your models here.

class OServico(admin.ModelAdmin):
	list_display = ('clientes','lista_produtos','tipo_servivo','data_entrega','status_servico')
	icon = '<i class="material-icons">work</i>'

admin.site.register(Ordem_Servico,OServico)