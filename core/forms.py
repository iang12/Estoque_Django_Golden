#coding:utf-8
from django import forms
from django.forms import Select,Textarea,TextInput,NumberInput,EmailInput,DateInput
from .models import *




class ClienteForm(forms.ModelForm):
    class Media:
        css = {
        'all': ('css/admin.css',)
        }
        
        js = ('jquery-1.8.3.min.js')
        js = ('jquery.maskedinput.min.js',)
        js = ('admin.js')