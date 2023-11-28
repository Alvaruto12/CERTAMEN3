from django.contrib import admin
from .models import Evento, Segmento, Tipo

# Register your models here.
admin.site.register(Tipo) 
admin.site.register(Evento) 
admin.site.register(Segmento) 
