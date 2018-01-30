from django import forms
from django.forms import Select,Textarea,TextInput,NumberInput,EmailInput
from vendas.models import *


class ServicoForm(forms.ModelForm):
    class Meta:
        model = Servicos
        exclude = ['']
        fields = '__all__'
        widgets = {
            'nome':TextInput(attrs={'class':'form-control','placeholder':'Nome do serviço'}),
            'preco':TextInput(attrs={'class':'form-control','placeholder':'Preço'})
        }
class OrdemServicoForm(forms.ModelForm):
    class Meta:
        model   = Ordem_Servico
        exclude = ['']
        fields  = '__all__'
        widgets = {
            'clientes': Select(attrs={'class': 'form-control','placeholder':'Clientes '}),
            'lista_produtos': TextInput(attrs={'class': 'form-control','placeholder':'EX:lista de Produtos'}),
            'status_servico': Select(attrs={'class': 'form-control','placeholder':'Status '}),
            'tipo_servivo':TextInput(attrs={'class':'form-control','placeholder':'EX:Manutenção '}),
            'data_emissao':TextInput(attrs={'class':'form-control','data-provide':'datepicker' ,'data-date-format':'dd/mm/yyyy','id':'data_emissao'}),
            'data_entrega':TextInput(attrs={'class':'form-control','data-provide':'datepicker' ,'data-date-format':'dd/mm/yyyy','id':'data_ini'}),
            'observacao':Textarea(attrs={'class':'form-control no-resize','rows':3,'placeholder':'Observação'}),
        }
