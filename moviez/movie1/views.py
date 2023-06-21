from django.shortcuts import render
from movie1.models import movie
from movie1.forms import movieform
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy


# Create your views here.
class MovieListView(ListView):
    model = movie
    template_name = "home.html"
    context_object_name = "img"


"""
def home(request):
    img = movie.objects.all()
    return render(request, 'home.html', {"img": img})



def view(request, pk):
    s = movie.objects.get(id=pk)
    return render(request, 'view.html', {"s": s})
"""


class MoviedetailView(DetailView):
    model = movie
    template_name = "view.html"
    context_object_name = "s"


"""
def update(request, p):
    b = movie.objects.get(id=p)
    f = movieform(instance=b)
    if (request.method == "POST"):
        print(request.POST)
        f = movieform(request.POST, instance=b)
        if (f.is_valid()):
            f.save()
        return home(request)

    return render(request, 'update.html', {'form': f})
"""


class Movieupdateview(UpdateView):
    model = movie
    template_name = "update.html"
    fields = ['title', 'description', 'img']
    success_url = reverse_lazy('movie1:home')


"""
def delete(request, p):
    b = movie.objects.get(id=p)
    b.delete()
    return home(request)
"""


class Moviedelete(DeleteView):
    model = movie
    template_name = "delete.html"
    success_url = reverse_lazy('movie1:home')


"""
def add(request):
    f = movieform()  # Creates Empty form object
    if (request.method == "POST"):
        print(request.POST)
        f = movieform(request.POST, request.FILES)
        if (f.is_valid()):
            f.save()
            return home(request)
    return render(request, 'add.html', {'form': f})
"""


class Movieaddview(CreateView):
    model = movie
    template_name = "add.html"
    fields = ['title', 'description', 'img']
    success_url = reverse_lazy('movie1:home')
