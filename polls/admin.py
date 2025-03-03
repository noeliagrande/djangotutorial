from django.contrib import admin

from .models import Question

# Register your models here.

# Registra el modelo Question en el sitio de administración de Django para gestionarlo desde la interfaz web.
admin.site.register(Question)