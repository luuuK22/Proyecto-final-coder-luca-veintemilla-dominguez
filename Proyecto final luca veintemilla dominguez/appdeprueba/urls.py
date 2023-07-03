from django.urls import path

from appdeprueba import views



urlpatterns = [
  
    
    path("inicio",views.home,name="inicio"),
    path("cursos/",views.cursos, name="Cursos"),
    path("estudiante/",views.estudiantes,name="estudiante"),
    path("profes/",views.profesores,name="Profes"),
    path("entregables/",views.entregables,name="Entregables"),
    path("Iniciar_sesion/",views.iniciar_sesion,name="Iniciar sesion"),
    path("cursoformulario",views.curso_formu,name="cursoformulario"),
    path("profeformulario",views.profe_formu,name="Profeformulario"),
    path("estudianteformulario",views.estudiantes_formu,name="estudianteformulario"),
    path("busquedacamada",views.busquedacamada,name="busquedacamada"),
    path("buscar/",views.buscar)

]