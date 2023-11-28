from django.db import models

class Tipo(models.Model):
    id = models.CharField(primary_key=True,max_length=3)
    nombre = models.CharField(max_length=100)
    def str(self) -> str:
        return self.nombre


class Segmento(models.Model):
    id = models.CharField(primary_key=True,max_length=3)
    nombre = models.CharField(max_length=100)
    def str(self) -> str:
        return self.nombre


class Evento(models.Model):

    fecha_inicio = models.DateField()
    fecha_termino = models.DateField()
    titulo = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=100)
    tipo = models.ForeignKey(Tipo, on_delete=models.CASCADE)
    segmento = models.ForeignKey(Segmento, on_delete=models.CASCADE)
    def str(self) -> str:
        return self.titulo
