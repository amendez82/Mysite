from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def index(request):
    return HttpResponse("hello world -> Bienvenido al modulo de Encuestas")

def detail(request, question_id):
    return HttpResponse("Pregunta %s." % question_id)

def results(request, question_id):
    response = "Resultado %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("Su voto para la pregunta %s." % question_id)