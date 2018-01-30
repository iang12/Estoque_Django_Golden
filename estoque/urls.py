# -*- coding: utf-8 -*-
from django.conf.urls import url
from estoque.views import *
from . import views

urlpatterns = [
   #categorias
    url(r'^categorias/$', ListaCategoria.as_view(), name = 'lista_categoria'),
    url(r'^categorias/add/$', Add_Categoria.as_view(), name='criar_categoria'),
    #url(r'^categorias/(?P<pk>\d+)/update/$', views.categoria_update, name='atualizar_categoria'),
    #url(r'^categorias/(?P<pk>\d+)/delete/$', views.categoria_delete, name='excluir_categoria'),
    #url(r'^detalhes/(?P<pk>\d+)/$', Detalhes.as_view(), name ='detalhe_categoria'),
    #produtos
    url(r'^produtos/$', Produtos.as_view(), name = 'produtos'),
    url(r'^produtos/add/$',Add_Produto.as_view(), name='novo_produto'),
    url(r'^produtos/atualizar(?P<pk>\d+)/$', AtualizarProduto.as_view(), name ='produto_update'),
    #url(r'^produtos/(?P<pk>\d+)/atualizar/$', views.atualizar_produto, name='atualizar_produto'),
    #url(r'^produtos/(?P<pk>\d+)/delete/$', views.produto_delete, name='excluir_produto'),'
    #entradas
    url(r'^estoque/adicionar/$',Entrada.as_view(),name="add_entradas")
]
