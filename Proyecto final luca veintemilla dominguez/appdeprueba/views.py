from django.shortcuts import render
from django.shortcuts import HttpResponse
from appdeprueba.forms import *
from appdeprueba.models import *


def home(request):
    return render(request, "appdeprueba/inicio.html")

def cursos(request):
    return render(request, "appdeprueba/cursos.html")

def profesores(request):
    return render(request, "appdeprueba/Profesor.html")

def estudiantes(request):
    return  render(request, "appdeprueba/Estudiante.html")

def entregables(request):
    return render(request, "appdeprueba/entregable.html")

def iniciar_sesion(request):
    return render(request, "appdeprueba/iniciar_sesion.html")


def curso_formu(request):
    if request.method == "POST":
        miFormulario = CursoFormulario(request.POST) # Aqui me llega la informacion del html
        print(miFormulario)
       
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            curso = Curso(nombre=informacion["curso"], camada=informacion["camada"])
            curso.save()
            return render(request, "appdeprueba/inicio.html")
    else:
        miFormulario = CursoFormulario()
    return render(request, "appdeprueba/cursoformulario.html", {"miFormulario": miFormulario})


def profe_formu(request):
    if request.method == "POST":
        miFormulario = profeformulario(request.POST) # Aqui me llega la informacion del html
        print(miFormulario)
       
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            profe = Profesor(nombre=informacion["nombre"], apellido=informacion["apellido"],
            email = informacion["email"])
            profe.save()
            return render(request, "appdeprueba/inicio.html")
    else:
        miFormulario = profeformulario()
    return render(request, "appdeprueba/profeformulario.html", {"miFormulario": miFormulario})

def estudiantes_formu(request):
    if request.method == "POST":
        miFormulario = Estudianteform(request.POST) # Aqui me llega la informacion del html
        print(miFormulario)
       
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            estudiante = Estudiante(nombre=informacion["nombre"], apellido=informacion["apellido"],
            email = informacion["email"])
            estudiante.save()
            return render(request, "appdeprueba/inicio.html")
    else:
        miFormulario = profeformulario()
    return render(request, "appdeprueba/estudianteformulario.html", {"miFormulario": miFormulario})

def busquedacamada(request):
    return render(request,"appdeprueba/templates/busquedacamada.html")

def buscar(request):

    if request.GET["camada"]:

        camada = request.GET['camada']
        cursos = Curso.objects.filter(camada__icontains=camada)
        return render(request, "appdeprueba/resultadosbusqueda.html", {"cursos": cursos, "camada":camada})
    
    else:
        respuesta = "no enviaste datos"
   
    return HttpResponse(respuesta)