from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse
#FUNCTION ORIENTED VIEWS

#HOME VIEW
def home(request):
    # return HttpResponse("<h1>Welcome to Django</h1>")
      return render(request,'home.html')


#INDEX VIEW
def index(request):
    # return HttpResponse("<h1>Hello Python</h1>")
    data = {'Name':'Aparna', 'Age':24}
    return render(request, 'index.html', data)