"""
URL configuration for proyectoprueba project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from xddd.views import nombre
from xddd.views import sumar
from xddd.views import probando_template
from xddd.views import diahoy
from xddd.views import prueba_loader_otra_plantilla
urlpatterns = [
    path("admin/", admin.site.urls),
    path("appdeprueba/",include("appdeprueba.urls")),
    path("nombre/<nombre>",nombre),
    path("sumar/<num>",sumar),
    path("probandotemplate/",probando_template),
    path("diahoy/",diahoy),
    path("pruebaotraplanti/<nombre>",prueba_loader_otra_plantilla)
    
]
