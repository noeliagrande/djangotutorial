from django.contrib import admin

from .models import Choice, Question

# Register your models here.

# Registra el modelo Question en el sitio de administración de Django para gestionarlo desde la interfaz web.
'''
# La clase muestra el campo pub_date antes que el campo question_text
class QuestionAdmin(admin.ModelAdmin):
    fields = ["pub_date", "question_text"]
'''

'''
# Muestra el campo question_text
# Muestra pub_date separado bajo la etiqueta "Date information"
class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ["question_text"]}),
        ("Date information", {"fields": ["pub_date"]}),
    ]
'''

# Los objetos Choice se editan en la página de administración de Question.
# Por defecto, proporciona suficientes campos para 3 opciones.
#class ChoiceInline(admin.StackedInline): # campos separados
class ChoiceInline(admin.TabularInline): # formato de tabla
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ["question_text"]}),
        ("Date information", {"fields": ["pub_date"], "classes": ["collapse"]}),
    ]
    inlines = [ChoiceInline]
    list_display = ["question_text", "pub_date", "was_published_recently"]

    # barra lateral permite filtrar la lista de cambios por el campo pub\_date
    list_filter = ["pub_date"]

    # cuadro de búsqueda (Search)
    search_fields = ["question_text"]

admin.site.register(Question, QuestionAdmin)