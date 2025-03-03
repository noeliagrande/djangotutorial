
# F se utiliza para realizar operaciones en la base de datos basadas en los valores de otros campos de un mismo modelo,
# sin necesidad de cargar esos valores en memoria.

from django.db.models import F
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic # proporciona vistas basadas en clases (CBVs: Class-Based Views).
                                 # Las vistas basadas en clases permiten organizar y reutilizar el código de una
                                 # manera más estructurada y concisa que las vistas basadas en funciones (FBVs).
from django.utils import timezone

from .models import Choice, Question


# IndexView hereda de ListView: está utilizando una vista genérica de Django para mostrar una lista de objetos.
# template_name: archivo de plantilla a usar.
# context_object_name: variable en el contexto de la plantilla que contiene los objetos que se van a mostrar.
# get_queryset: get_queryset: método para obtener los objetos de la base de datos (las últimas 5 preguntas)
class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        """
        Return the last five published questions (not including those set to be
        published in the future).
        """
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by("-pub_date")[:5]


# vista 'detail'
class DetailView(generic.DetailView):
    model = Question
    template_name = "polls/detail.html"

    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())


# vista 'results'
class ResultsView(generic.DetailView):
    model = Question
    template_name = "polls/results.html"


def vote(request, question_id):
    # obtener un objeto de la base de datos o devolver un error 404 si no se encuentra el objeto
    question = get_object_or_404(Question, pk=question_id)
    try:
        # choice_set: acceder a todas las opciones (Choice) relacionadas con una instancia del modelo Question.
        # get(): está buscando un objeto Choice cuyo pk coincida con el valor enviado a través del formulario.
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(
            request,
            "polls/detail.html",
            {
                "question": question,
                "error_message": "You didn't select a choice.",
            },
        )
    else:
        selected_choice.votes = F("votes") + 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))
