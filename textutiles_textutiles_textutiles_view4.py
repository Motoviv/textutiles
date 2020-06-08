from django.http import HttpResponse
from django.shortcuts import render
#Ex of templete-2

def index2(request):
    return render(request, 'index2.html')

def analyze(request):
    #get the text
     djangotext=request.GET.get('text','default')
     removepunc=request.GET.get('removepunc','off')
     print(removepunc)
     print(djangotext)
#analyse the text
     return HttpResponse("remove punc")