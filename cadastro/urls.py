# -*- coding: utf-8 -*-
from django.conf.urls import url
from . import views

urlpatterns = [
    # Cliente
    url(r'clientes/$',views.Clientes.as_view(), name='lista_clientes'),
    url(r'cliente/adicionar/$', views.AdicionarCliente.as_view(), name='add_cliente'),
    url(r'cliente/atualizar/(?P<pk>\d+)/$', views.AtualizarCliente.as_view(), name='cliente-update'),
    #url(r'cliente/editar/(?P<pk>[0-9]+)/$',views.EditarCliente.as_view(), name='editar_clientes'),
]
