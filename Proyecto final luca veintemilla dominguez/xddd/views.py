from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from django.template import Template,Context
from datetime import *
from django.template import loader

def probando_template(self):
    dia_de_hoy = datetime.now()
    nombre = "luca"
    apellido = "veintemilla"
    notas = [1,4,2,6,7,4,2,8,5]
    edad = 19
    dicc = {"nombre":nombre,"apellido":apellido,"edad":edad,"dia":dia_de_hoy,"notas":notas}



    plantilla = loader.get_template("template.html")


    documento = plantilla.render(dicc)
        
    return HttpResponse(documento)

def prueba_loader_otra_plantilla(self,nombre):
    dia = datetime.now()
    dicc = {"nombre":nombre,"diahoy":dia}

    plantilla = loader.get_template("prueba.html")
    
    doc = plantilla.render(dicc)
    return HttpResponse(doc)


def nombre(self,nombre):
    doc = f"mi nombre es : <br> {nombre}"

    return HttpResponse(doc)


def sumar(self,num):
    num = int(num)
    result =  num+num
    
    return HttpResponse(f"el resultado de la suma fue: {result}")


def diahoy(self):
    hoy = datetime.date()
    return HttpResponse(hoy)


def home(request):
    return HttpResponse("vista de inicio")

def cursos(request):
    return HttpResponse("vista cursos")