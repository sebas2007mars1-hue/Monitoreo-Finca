
from django.urls import path
from .views import TemperaturaAPIView, SueloAPIView

urlpatterns = [
    path(
        "temperatura/",
        TemperaturaAPIView.as_view(),
        name="temperatura"
    ),
    path(
        "suelo/",
        SueloAPIView.as_view(),
        name="suelo"
    ),
]