from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
import json
from .models import *

# Create your views here.
@api_view(["POST", "GET", "PUT", "DELETE"])
def peliculas(request):
    result = {"status": 400}
    if request.method == "POST":
        _pelicula = Pelicula.objects.create(
            titulo = "Marvel"+str(len(Pelicula.objects.all()) + 1)
        )
        for i in range(3):
            Puesto.objects.create(
                pelicula = _pelicula
            )
        result = {"status":200, "message":"Guardado correctamente."}
        # consulta de base de datos y da una respusta indicando que se guardo correctamente.
    elif request.method == "GET":
        _peliculas = Pelicula.objects.all()
        result = []
        for pelicula in _peliculas:
            puestos = {}
            cont = 0
            for puesto in Puesto.objects.filter(pelicula = pelicula):
                puestos[str(puesto.pk)] = puesto.status
                if puesto.status:
                    cont += 1
                    
            result.append({"titulo":pelicula.titulo, "puestos": puestos, "cont": cont})
    elif request.method == "PUT":
        puesto = str(request.data["puesto"])
        status_puesto = request.data["status_puesto"]
        p = Puesto.objects.filter(pk = puesto).first()
        p.status = status_puesto
        p.save()

        result = {"status":200, "message":"Actualizado correctamente."}
    elif request.method == "DELETE":
        Pelicula.objects.filter(titulo = request.data["titulo"]).delete()

        result = {"status":200, "message":"Eliminado correctamente."}

    return Response(result)