# -*- coding: utf-8 -*-
from django.shortcuts import render,redirect
#views.py
from django.views.generic import *
from login.forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext

@login_required
def register(request):
    template_name='registration/register.html'
    if request.method=='POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('dashboard')
    else:
        form= RegisterForm()
    context={
        'form':form
    }
    return render(request,template_name,context)
 
def register_success(request):
    return render_to_response(
    'registration/success.html',
    )
 
def logout_page(request):
    logout(request)
    return HttpResponseRedirect('/')
"""
@login_required
def home(request):
    return render_to_response(
    'home.html',
    { 'user': request.user }
    )
"""
class UsuariosListView(ListView):
    template_name = 'usuarios.html'
    model = User
    context_object_name = 'users'

    def get_queryset(self):
        return User.objects.all()
