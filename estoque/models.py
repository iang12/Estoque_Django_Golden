# -*- coding: utf-8 -*-
from django.db import models
import datetime
from django.db.models import signals
from django.core.validators import MinValueValidator
from decimal import Decimal
class Categoria(models.Model):
    categoria  = models.CharField( max_length=50,unique=True)
    criado     = models.DateField(auto_now_add=True)
    def __str__(self):
        return self.categoria
    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

class Produto(models.Model):
    produto = models.CharField('Produto', max_length=100, unique=True)
    importado = models.BooleanField('Importado', default=False)
    preco_venda = models.DecimalField('Preço De Venda',max_digits=7,decimal_places=2)
    preco_compra = models.DecimalField('Preço De Compra',max_digits=7,decimal_places=2)
    ipi = models.DecimalField(
        'IPI', max_digits=3, decimal_places=2,blank=True)
    estoque = models.IntegerField('Estoque atual',blank=False, null=False, default=0)
    estoque_min = models.PositiveIntegerField('Estoque mínimo', default=0)
    category = models.ForeignKey(Categoria, verbose_name='categoria',null=True, blank=True)
    descricao = models.CharField('Observação',blank=False, max_length=300)
    data_de_cadastro = models.DateField(auto_now_add=True)
    class Meta:
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'
    def __str__(self):
        return self.produto
    def get_price(self):
        return "R$ %s" % number_format(self.preco_venda, 2)

class Entradas_Estoque(models.Model):
    data = models.DateField(auto_now_add=True)
    categoria = models.ForeignKey('Categoria', verbose_name='categoria',null=True, blank=True)
    produto   = models.ForeignKey('Produto',on_delete=models.CASCADE, null=True, blank=True)
    quantidade = models.DecimalField(max_digits=13, decimal_places=2, validators=[
    MinValueValidator(Decimal('0.00'))], null=True, blank=True)
    observacao= models.TextField(blank=True)

def update_stock(sender, instance, **kwargs):
    instance.produto.estoque += instance.quantidade
    instance.produto.save()
# register the signal
signals.post_save.connect(update_stock, sender=Entradas_Estoque, dispatch_uid="update_stock_count")
