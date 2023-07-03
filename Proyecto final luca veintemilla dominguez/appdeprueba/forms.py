from django import forms


class CursoFormulario(forms.Form):
    curso = forms.CharField()
    camada = forms.IntegerField()

class profeformulario(forms.Form):
    nombre = forms.CharField()
    apellido = forms.CharField()
    email = forms.EmailField()    


class Entregable(forms.Form):
    nombre = forms.CharField()
    fecha_de_entrega = forms.DateField()
    entregado = forms.BooleanField()

class Estudianteform(forms.Form):
    nombre = forms.CharField()
    apellido = forms.CharField()
    email = forms.EmailField()
    
    