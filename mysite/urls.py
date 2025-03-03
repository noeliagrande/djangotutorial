"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.contrib import admin # Permite acceder al panel de administración de Django.
from django.urls import include, path # include: para incluir las rutas de otras apps dentro del proyecto.
                                      # path: para definir rutas

urlpatterns = [
    path("polls/", include("polls.urls")), #Redirige cualquier URL que comience con "polls/" al archivo polls/urls.py
    path('admin/', admin.site.urls), # Habilita el panel de administración de Django en http://localhost:8000/admin/.
]
