#i have created tis file-srija
 # code for vidio 5
from django.http import HttpResponse
def index(request):
    return HttpResponse('''<h1>open the link</h1> <a href="https://www.amazon.in/"> DJANGO CODEING </a>''')
#ans of exersise1
def ex1(request):
     s='''<h2> Navigation Bar<br></h2> 
     <a href="https://www.facebook.com/">FACEBOOK</a> <br>
     <a href="https://www.myntra.com">MYNTRA</a> <br>
     <a href="https://www.udemy.com/">PYTHON</a> <br>
     <a href="https://www.flipkart.com/">FLIPKART</a> <br>'''
     return HttpResponse(s)