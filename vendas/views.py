# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.views.generic import CreateView, DeleteView, TemplateView, UpdateView, ListView, DetailView
from vendas.forms import *
from django.contrib.messages.views import SuccessMessageMixin
class Servicos(ListView):
    context_object_name = 'servicos'
    model = Servicos
    template_name = 'servicos/servicos.html'
class Servicos_Add(CreateView):
	form_class = ServicoForm
	template_name = 'servicos/servicos_add.html'
	model = Servicos
	success_url='/servicos'
	success_message = " Adicionado Com Sucesso"
class Os_Serv(ListView):
    context_object_name = 'os_serv'
    model = Ordem_Servico
    template_name = 'os.html'
class Os_Add(CreateView):
	form_class = OrdemServicoForm
	template_name = 'os_add.html'
	model = Ordem_Servico
	sucess_url = '/os'
	success_message = " Adicionado Com Sucesso"
