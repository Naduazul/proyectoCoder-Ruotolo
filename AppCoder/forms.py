from django import forms


class citasFormulario (forms.Form):
    nombre = forms.CharField()
    codigo = forms.IntegerField()
    
class profesionalesFormulario (forms.Form):
    nombre = forms.CharField()
    apellido = forms.CharField()
    email = forms.EmailField()
    cargo = forms.CharField()