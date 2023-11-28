from rest_framework import serializers
from miapp.models import Evento

class EventoSerializer(serializers.ModelSerializers):
  class Meta:
    model=Evento
    fields='__all__'
