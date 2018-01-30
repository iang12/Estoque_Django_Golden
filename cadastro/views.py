from django.shortcuts import render
from django.views.generic import *
from cadastro.models import *
from cadastro.forms import *
from django.contrib.messages.views import SuccessMessageMixin
# Create your views here.
class Clientes(ListView):
	context_object_name = 'clientes'
	model = Cliente
	template_name = 'clientes.html'

class AdicionarCliente(SuccessMessageMixin,CreateView):
	form_class = ClienteForm
	template_name = 'add_cliente.html'
	model = Cliente
	success_url = '/clientes'
	success_message = "Cliente Adicionado Com Sucesso"

class AtualizarCliente(SuccessMessageMixin,UpdateView):
	form_class = ClienteForm
	template_name = 'add_cliente.html'
	model = Cliente
	success_url='/clientes'
	success_message = "Dados Atualizados Com Sucesso"
