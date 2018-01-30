# -*- coding: utf-8 -*-
from django.db import models
from vendas.choices import *
from cadastro.models import Cliente
import datetime
class Servicos(models.Model):
	nome  = models.CharField( max_length=50)
	preco = models.CharField( max_length=5)
	data_cadastro  = models.DateField(auto_now_add=True)
	def __str__(self):
		return self.nome 

class Ordem_Servico(models.Model):
	clientes      = models.ForeignKey(Cliente,verbose_name='Cliente')
	lista_produtos= models.CharField('Produto Deixado', max_length=50)
	tipo_servivo  = models.CharField('Tipo Do Serviço',max_length=50)
	data_entrega  = models.DateField('Data de entrega')
	status_servico= models.CharField('Status Do Serviço',choices=STATUS, max_length=2,default='P')
	observacao    = models.TextField('Relatório')
	data_emissao  = models.DateField('Data De Emissão')
	def __str__(self):
		return self.tipo_servivo 

	class Meta:
		verbose_name='Ordem de Serviço'
		verbose_name_plural='Ordem de Serviços'




