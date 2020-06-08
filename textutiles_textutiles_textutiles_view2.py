#code for vidio 7 -laying the pipeline
from django.http import HttpResponse

def index(request):
    return HttpResponse("Home")

def removepunc(request):
    return HttpResponse("remove punc")

def capfirst(request):
    return HttpResponse("Captalize first")

def newlineremove (request):
    return HttpResponse(" new line remover")

def spaceremove(request):
     return HttpResponse("space remover <a href = '/'> back </a>")

def charcount(request):
     return HttpResponse("char count")
