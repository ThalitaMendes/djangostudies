from django import forms
from .models import Cliente

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Clientes
        fields = ['nome', 'sexo', 'data_nascimento','email','profissao']