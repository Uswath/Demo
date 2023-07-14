from django.shortcuts import render
from app1.models import place,team


def base(request):
    p = place.objects.all()
    t = team.objects.all()
    return render(request, 'index.html', {'p': p, 't': t})


