# -*- coding: utf-8 -*-
from django.conf.urls import url
from vendas.views import *
from . import views

urlpatterns = [
	url(r'^servicos/$',Servicos.as_view(), name='servicos'),
	url(r'^servicos/add/$',Servicos_Add.as_view(),name='add_servicos'),
	url(r'^os/$',Os_Serv.as_view(), name='os_serv'),
	url(r'^os/add/$', Os_Add.as_view(), name = 'add_os'),
]
