"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
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
from django.http import HttpResponse
from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions


schema_view = get_schema_view(
    openapi.Info(
        title="API Monitoreo de Finca",
        default_version="v1",
        description="Sistema de monitoreo de temperatura y humedad del suelo",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


def inicio(request):
    html = """
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Monitoreo de Finca</title>
        <style>
            body {
                margin: 0;
                font-family: Arial, sans-serif;
                background: #f0f4f0;
                color: #26352b;
                text-align: center;
            }
            header {
                background: #246b45;
                color: white;
                padding: 35px 15px;
            }
            main {
                max-width: 750px;
                margin: 45px auto;
                padding: 20px;
            }
            .menu {
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
                gap: 18px;
                margin-top: 30px;
            }
            .card {
                background: white;
                padding: 25px 15px;
                border-radius: 12px;
                box-shadow: 0 3px 12px #00000015;
            }
            .card h2 {
                color: #246b45;
            }
            .btn {
                display: inline-block;
                background: #246b45;
                color: white;
                padding: 12px 20px;
                border-radius: 8px;
                text-decoration: none;
                margin-top: 10px;
            }
            .btn:hover {
                background: #174b30;
            }
            footer {
                margin-top: 50px;
                padding: 20px;
                color: #657268;
            }
        </style>
    </head>
    <body>
        <header>
            <h1>🌱 Monitoreo de Finca</h1>
            <p>Sistema de monitoreo de temperatura y humedad del suelo</p>
        </header>

        <main>
            <h2>Panel principal</h2>
            <p>Selecciona una opción para continuar.</p>

            <div class="menu">
                <div class="card">
                    <h2>🔐 Administración</h2>
                    <p>Accede al panel administrativo de Django.</p>
                    <a class="btn" href="/admin/">Ingresar</a>
                </div>

                <div class="card">
                    <h2>📘 Swagger</h2>
                    <p>Consulta y prueba los endpoints de la API.</p>
                    <a class="btn" href="/swagger/">Abrir Swagger</a>
                </div>

                <div class="card">
                    <h2>📄 ReDoc</h2>
                    <p>Consulta la documentación de la API.</p>
                    <a class="btn" href="/redoc/">Abrir ReDoc</a>
                </div>

                <div class="card">
                    <h2>🌡️ API</h2>
                    <p>Accede a los endpoints de monitoreo.</p>
                    <a class="btn" href="/api/">Ver API</a>
                </div>
            </div>
        </main>

        <footer>
            Proyecto Monitoreo de Finca
        </footer>
    </body>
    </html>
    """
    return HttpResponse(html)


urlpatterns = [
    path("", inicio, name="inicio"),
    path("admin/", admin.site.urls),
    path("api/", include("monitoreo.urls")),
    path(
        "swagger/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    path(
        "redoc/",
        schema_view.with_ui("redoc", cache_timeout=0),
        name="schema-redoc",
    ),
]