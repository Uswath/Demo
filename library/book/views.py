from django.shortcuts import render
from book.models import book, student
from book.forms import bookform
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse


# Create your views here.
def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def add(request):
    if (request.method == "POST"):
        t = request.POST['t']
        a = request.POST['a']
        p = request.POST['p']
        d = request.FILES['d']
        c = request.FILES['c']
        b = book.objects.create(title=t, author=a, price=p, pdf=d, cover=c)
        b.save()
        return home(request)

    return render(request, 'add.html')


def view(request):
    b = book.objects.all()
    return render(request, 'view.html', {'book': b})


def view_book(request, p):
    b = book.objects.get(id=p)
    return render(request, 'viewbook.html', {'book': b})


def delete_book(request, p):
    b = book.objects.get(id=p)
    b.delete()
    return view(request)


def edit_book(request, p):
    b = book.objects.get(id=p)
    form = bookform(instance=b)
    if (request.method == "POST"):
        print(request.POST)
        f = bookform(request.POST, request.FILES, instance=b)
        if (f.is_valid()):
            f.save()
            return home(request)

    return render(request, 'add2.html', {'form': form})


def search(request):
    if request.method == "POST":
        s = request.POST['srh']
        if s:
            match = book.objects.filter(Q(title__icontains=s) | Q(author__icontains=s))
            if match:
                return render(request, 'search.html', {'m': match})
            else:
                messages.error(request, "No Results Found")

    return render(request, 'search.html')


def register(request):
    if request.method == "POST":
        u = request.POST['u']
        f = request.POST['f']
        l = request.POST['l']
        e = request.POST['e']
        p = request.POST['p']
        cp = request.POST['cp']
        if p == cp:
            user = User.objects.create_user(username=u, first_name=f, last_name=l, email=e, password=p)
            user.save()
            return home(request)
    return render(request, 'register.html')


def user_login(request):
    if request.method == "POST":
        u = request.POST['u']
        p = request.POST['p']
        user = authenticate(username=u, password=p)
        if user:
            login(request, user)
            return home(request)
        else:
            messages.error(request, "Invalid Credentials")
    return render(request, 'login.html')


def user_logout(request):
    logout(request)
    return home(request)


def view1(request):
    c = student.objects.all()
    return render(request, 'view1.html', {'student': c})


def add1(request):
    if (request.method == "POST"):
        f = request.POST['f']
        l = request.POST['l']
        a = request.POST['a']
        p = request.POST['p']
        s = student.objects.create(first_name=f, last_name=l, age=a, place=p)
        s.save()
        return home(request)

    return render(request, 'add1.html')


def add2(request):
    f = bookform()  # Creates Empty form object
    if (request.method == "POST"):
        print(request.POST)
        f = bookform(request.POST, request.FILES)  # Creates form objects using values recieved from form
        # request.POST -dictionary sent from template
        if (f.is_valid()):
            f.save()
            return home(request)
    return render(request, 'add2.html', {'form': f})


def fact1(request):
    if (request.method == "POST"):
        n1 = int(request.POST['n1'])
        f = 1
        for i in range(1, n1 + 1):
            f = f * i

        return render(request, 'fact.html', {'fact1': f})

    return render(request, 'fact.html')


def calculation(request):
    if (request.method == "POST"):
        n1 = int(request.POST['n1'])
        n2 = int(request.POST['n2'])
        add = n1 + n2
        sub = n1 - n2
        mul = n1 * n2
        div = n1 / n2
        return render(request, 'result.html', {'sum': add, 'difference': sub, 'multiplication': mul, 'division': div})
    return render(request, 'calc.html')
