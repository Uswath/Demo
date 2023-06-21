from django.shortcuts import render
from moviee.models import movies


# Create your views here.
def base(request):
    a = movies.objects.all()
    return render(request,'base.html',{'a': a})
