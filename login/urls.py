# -*- coding: utf-8 -*-
from django.conf.urls import url
from login.views import *
from django.contrib.auth.models import *
from django.contrib.auth import views as auth_views
urlpatterns = [
    url(r'^$', auth.views.login),
    url(r'^register/$', register),
    url(r'^register/success/$',register_success),
    url(r'^logout/$', logout_page),
    #/login/usuarios/
    url(r'^usuarios/$',UsuariosListView.as_view(), name='usuarios'),

]
