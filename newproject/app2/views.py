from django.shortcuts import render


from django.http import HttpResponse

def first(request):
    # return HttpResponse("<h1>First Page</h1>")
    return render(request, 'first.html')

def second(request):
    # return HttpResponse("<h1>Second Page</h1>")
    return render(request, 'second.html')