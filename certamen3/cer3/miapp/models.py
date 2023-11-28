from django.db import models

# Create your models here.

class Tipo(models.Model):
    TIPO_CHOICES = [
        ("I","Info"),
        ("V", "Vacaciones"),
        ("F", "Feriado"),
        ("SA", "Suspension de actividades"),
        ("SAPM", "Suspension de actividades PM"),
        ("PL", "Periodo Lectivo"),
        ("SE", "Suspension de Evaluaciones"),
        ("C", "Ceremonia"),
        ("ED", "EDDA"),
        ("EV", "Evaluacion"),
        ("A", "Ayudantias"),
        ("HA", "Hito Academico"),
        ("SA", "Secretaria Academica"),
        ("OA", "OAI"),
    ]
    tipo = models.CharField(max_length=4, choices=TIPO_CHOICES, default='I')

    def __str__(self):
        texto="{0}"
        return texto.format(self.tipo)


class Segmento(models.Model):
    TIPO_CHOICES = [
        ("C","Comunidad USM"),
        ("E", "Estudiante"),
        ("P", "Profesor"),
        ("J", "Jefe de Carrera"),
    ]

    tipo = models.CharField(max_length=1, choices=TIPO_CHOICES, default='C')

    def __str__(self):
        texto="{0}"
        return texto.format(self.tipo)
    

class Evento(models.Model):

    fecha_inicio = models.DateField()
    fecha_termino = models.DateField()
    titulo = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=100)
    tipo = models.ForeignKey(Tipo, on_delete=models.CASCADE)
    segmento = models.ForeignKey(Segmento, on_delete=models.CASCADE)

    def __str__(self):
        texto="{0} ({1})"
        return texto.format(self.tipo,self.segmento)
