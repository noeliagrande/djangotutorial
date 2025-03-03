'''
Cada campo está representado por una instancia de una clase Field.
El nombre de cada instancia de Field será también el nombre de la columna en la base de datos.

Cuando se define un modelo, hay que crear y aplicar migraciones para que Django cree las tablas
correspondientes en la base de datos:

python manage.py makemigrations polls
python manage.py migrate polls
'''

import datetime

from django.contrib import admin
from django.db import models
from django.utils import timezone

'''
clase Question: modelo que se mapeará a una tabla en la base de datos.

question_text: campo de texto para la pregunta de la encuesta, con un límite de 200 caracteres.
pub_date: campo de fecha y hora para el momento en que la pregunta fue publicada. 
          El parámetro "date published" es solo una etiqueta que se mostrará en el panel de administración de Django
__str__(self): Este método define cómo representar un objeto cuando se convierte a una cadena de texto:
               devolverá el valor del question_text (al imprimir un objeto Choice, se verá el texto de la opción como una cadena)
               
 was_published_recently: determina si una pregunta fue publicada en las últimas 24 horas
'''
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")

    def __str__(self):
        return self.question_text

    # Hace que se muestre "Published recently?" en la tabla en vez de "was_published_recently"
    @admin.display(
        boolean=True,
        ordering="pub_date",
        description="Published recently?",
    )

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

'''
clase Choice: representa una respuesta a una pregunta

question: define una relación de clave foránea entre Choice y Question. (relación de uno a muchos entre Question y Choice).
          Una pregunta puede tener varias opciones de respuesta. Cada Choice está vinculado a una única Question.
          on_delete (CASCADE): si se elimina una pregunta (Question), todas las respuestas asociadas (Choice) también se eliminarán.
choice_text: campo de texto para el texto de la opción de respuesta, con un límite de 200 caracteres.
votes: campo para contar el número de votos que recibe cada opción de respuesta. Inicialmente, este valor es 0.
'''
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text