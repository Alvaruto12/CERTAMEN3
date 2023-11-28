from django.shortcuts import render
from django.http import HttpResponse
from .models import *

def index(request):
    title = "Inicio"
    segmentos = Segmento.objects.all()
    tipos = Tipo.objects.all()
    data = {
        "title": title,
        "total_segmentos": segmentos,
        "total_tipos": tipos
    }

    return render(request,'miapp/index.html', data)