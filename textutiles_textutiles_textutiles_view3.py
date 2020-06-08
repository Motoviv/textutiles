from django.http import HttpResponse
from django.shortcuts import render
#Ex of templete

def index(request):
 #3 rd argument we can pass dictionary
 params={'name':'anu','place':'earth'}
 return render(request,'index.html',params)