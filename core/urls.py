# -*- coding: utf-8 -*-
from django.conf.urls import include, url
from django.views.generic import TemplateView

from . import views

urlpatterns = [
	url(r'dashboard/$', views.dashboard),
]