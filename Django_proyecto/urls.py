"""Django_proyecto URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path, include
from django.contrib import admin
from temas import views
from django.contrib.admindocs import urls as admindocs_urls

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('admin/', admin.site.urls),
    path('registro/', views.registrarse, name='registrarse'),
    path('temas/', views.temas, name='temas'),
    path('temas_completados/', views.temas_completados, name='temas_completados'),
    path('cerrar_sesion/', views.cerrar_sesion, name='cerrar_sesion'),
    path('iniciar_sesion/', views.iniciar_sesion, name='iniciar_sesion'),
    path('crear_tema/', views.crear_tema, name='crear_tema'),
    path('temas/<int:tema_id>/', views.detalle_tema, name='detalle_tema'),
    path('temas/<int:tema_id>/completado/', views.completar_tema, name='completar_tema'),
    path('temas/<int:tema_id>/eliminar/', views.eliminar_tema, name='eliminar_tema'),
    
]