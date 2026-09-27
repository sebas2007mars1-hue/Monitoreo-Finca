
from rest_framework import serializers


# EJERCICIO 1: TEMPERATURA

class TemperaturaEntradaSerializer(serializers.Serializer):
    zona = serializers.CharField(max_length=100)
    temperatura = serializers.DecimalField(
        max_digits=5,
        decimal_places=2
    )
    fecha = serializers.DateField()
    hora = serializers.TimeField()


class TemperaturaSalidaSerializer(serializers.Serializer):
    mensaje = serializers.CharField()
    zona = serializers.CharField()
    temperatura = serializers.DecimalField(
        max_digits=5,
        decimal_places=2
    )
    fecha = serializers.DateField()
    hora = serializers.TimeField()
    estado = serializers.CharField()


# EJERCICIO 2: ESTADO DEL SUELO

class SueloEntradaSerializer(serializers.Serializer):
    cultivo = serializers.CharField(max_length=100)
    humedad = serializers.IntegerField(min_value=0, max_value=100)
    tipo_suelo = serializers.CharField(max_length=100)
    zona = serializers.CharField(max_length=100)


class SueloSalidaSerializer(serializers.Serializer):
    mensaje = serializers.CharField()
    cultivo = serializers.CharField()
    humedad = serializers.IntegerField()
    tipo_suelo = serializers.CharField()
    zona = serializers.CharField()
    alerta = serializers.CharField()