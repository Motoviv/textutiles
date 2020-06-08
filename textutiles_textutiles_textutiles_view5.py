from django.http import HttpResponse
from django.shortcuts import render
#Ex of templete-2

def index2(request):
    return render(request, 'index2.html')

def analyze(request):
    #get the text
     djangotext=request.POST.get('text','default')
#check checkbox value
     removepunc=request.POST.get('removepunc','off')
     fullcaps=request.POST.get('fullcaps','off')
     newlineremover=request.POST.get('newlineremover','off')
     spaceremover=request.POST.get('spaceremover','off')
     charcount=request.POST.get('charcount','off')
     print(removepunc)
     print(djangotext)
     if removepunc =="on":
#analyse the text
        analysed= djangotext
        punctuations ='''!"#$%&'()*+, -./:;<=>?@[\]^_`{|}~'''
        analyzed= ""
        for char in djangotext:
            if char not in punctuations:
                 analyzed = analyzed + char
        params ={'purpose':'Removed Punctuations','analyzed_text':analyzed}

        dajangotext=analyzed # to work all butons together
       # return render(request,'analyze.html',params)

     if(fullcaps=="on"):
         analyzed=""
         for char in djangotext:
             analyzed = analyzed + char.upper()
         params = {'purpose':'Changed to uppercase','analyzed_text':analyzed}
         dajangotext = analyzed  # to work all butons together
         dajangotext = analyzed  # to work all butons together

         #return render(request,'analyze.html',params)

     if(newlineremover=="on"):
         analyzed = ""
         for char in djangotext:
             if char !="\n" and char!="\r":
              analyzed = analyzed + char
         params = {'purpose': 'Removed new lines', 'analyzed_text': analyzed}
         dajangotext = analyzed  # to work all butons together

        # return render(request, 'analyze.html', params)
     if (spaceremover == "on"):
         analyzed = ""
         for index,char in enumerate(djangotext):
             if djangotext[index] == " " and djangotext[index+1] == " ":
                 pass
             else:
                 analyzed = analyzed + char
         params = {'purpose': 'space remover', 'analyzed_text': analyzed}
         dajangotext = analyzed  # to work all butons together

         #return render(request, 'analyze.html', params)

     if (charcount == "on"):
         analyzed = ""
         analyzed =  len(djangotext)
         params = {'purpose': 'NO OF CHARACTERS', 'analyzed_text': analyzed}
         dajangotext = analyzed  # to work all buttons

         #return render(request, 'analyze.html', params)
     if(removepunc!="on" and fullcaps !="on" and newlineremover !="on" and spaceremover!="on" and charcount != "on"):
         return HttpResponse("ERROR")

     return render(request, 'analyze.html', params)
