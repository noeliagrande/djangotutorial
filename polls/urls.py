from django.urls import path # para definir rutas

from . import views #  archivo views.py de la aplicación,
                       # donde están definidas las funciones de las vistas.

app_name = "polls" #namespace de la aplicación
urlpatterns = [
    # ex: /polls/: la ruta http://localhost:8000/polls/ ejecutará index()
    # "" → Ruta vacía significa que es la página principal de polls/.
    # IndexView es una clase dentro de views.py, basada en una clase genérica de Django
    # .as_view() es necesario para convertir la clase en una vista que pueda ser utilizada en las URL,
    #            ya que las vistas basadas en clases no se llaman directamente como las vistas basadas en funciones.
    # name="index" → Nombre de la URL para referenciarla en plantillas o redirecciones.
    path("", views.IndexView.as_view(), name="index"),

    # ex: /polls/5/: Si el usuario visita /polls/5/, question_id será 5.
    # <int:pk>: captura un valor entero de la URL y lo pasa como argumento a la vista.
    # views.DetailView.as_view() → Llama a la vista detail.
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),

    # ex: /polls/5/results/: /polls/5/results/ mostrará los resultados de la pregunta con ID 5.
    # <int:question_id>/results/ → Ruta para ver los resultados de una pregunta.
    # views.ResultsView.as_view() → Llama a la vista results.
    path("<int:pk>/results/", views.ResultsView.as_view(), name="results"),

    # ex: /polls/5/vote/: /polls/5/vote/ permitirá votar en la pregunta 5.
    # <int:question_id>/vote/ → Ruta para votar en una pregunta específica.
    # views.vote → Llama a la vista vote.
    path("<int:question_id>/vote/", views.vote, name="vote"),
]