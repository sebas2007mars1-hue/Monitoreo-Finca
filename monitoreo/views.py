
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema

from .serializers import (
    TemperaturaEntradaSerializer,
    TemperaturaSalidaSerializer,
    SueloEntradaSerializer,
    SueloSalidaSerializer
)


# EJERCICIO 1: REGISTRO DE TEMPERATURA

class TemperaturaAPIView(APIView):

    @swagger_auto_schema(
        operation_summary="Consultar servicio de temperatura",
        operation_description="Verifica que el endpoint de temperatura funciona.",
        responses={200: "Servicio disponible"}
    )
    def get(self, request):
        return Response(
            {
                "mensaje": "Servicio de temperatura funcionando correctamente",
                "metodos": ["GET", "POST"]
            },
            status=status.HTTP_200_OK
        )

    @swagger_auto_schema(
        operation_summary="Registrar temperatura",
        operation_description="Registra la temperatura de una zona del cultivo.",
        request_body=TemperaturaEntradaSerializer,
        responses={201: TemperaturaSalidaSerializer}
    )
    def post(self, request):
        serializer = TemperaturaEntradaSerializer(data=request.data)

        if serializer.is_valid():
            datos = serializer.validated_data
            temperatura = datos["temperatura"]

            if temperatura < 18:
                estado = "Baja"
            elif temperatura <= 30:
                estado = "Normal"
            else:
                estado = "Alta"

            respuesta = {
                "mensaje": "Temperatura registrada correctamente",
                "zona": datos["zona"],
                "temperatura": temperatura,
                "fecha": datos["fecha"],
                "hora": datos["hora"],
                "estado": estado
            }

            salida = TemperaturaSalidaSerializer(data=respuesta)
            salida.is_valid(raise_exception=True)

            return Response(
                salida.data,
                status=status.HTTP_201_CREATED
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )


# EJERCICIO 2: ESTADO DEL SUELO Y ALERTAS

class SueloAPIView(APIView):

    @swagger_auto_schema(
        operation_summary="Consultar servicio del suelo",
        operation_description="Verifica que el endpoint de suelo funciona.",
        responses={200: "Servicio disponible"}
    )
    def get(self, request):
        return Response(
            {
                "mensaje": "Servicio de monitoreo del suelo funcionando correctamente",
                "metodos": ["GET", "POST"]
            },
            status=status.HTTP_200_OK
        )

    @swagger_auto_schema(
        operation_summary="Registrar estado del suelo",
        operation_description="Registra la humedad y genera una alerta automática.",
        request_body=SueloEntradaSerializer,
        responses={201: SueloSalidaSerializer}
    )
    def post(self, request):
        serializer = SueloEntradaSerializer(data=request.data)

        if serializer.is_valid():
            datos = serializer.validated_data
            humedad = datos["humedad"]

            if humedad < 30:
                alerta = "Requiere riego"
            elif humedad <= 70:
                alerta = "Humedad adecuada"
            else:
                alerta = "Exceso de humedad"

            respuesta = {
                "mensaje": "Estado del suelo registrado correctamente",
                "cultivo": datos["cultivo"],
                "humedad": humedad,
                "tipo_suelo": datos["tipo_suelo"],
                "zona": datos["zona"],
                "alerta": alerta
            }

            salida = SueloSalidaSerializer(data=respuesta)
            salida.is_valid(raise_exception=True)

            return Response(
                salida.data,
                status=status.HTTP_201_CREATED
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )