"""
URL configuration for library project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from book import views
app_name = "book"
urlpatterns = [

    path('', views.home, name="home"),
    path('about', views.about, name="about"),
    path('add', views.add, name="add"),
    path('view', views.view, name="view"),
    path('view1', views.view1, name="view1"),
    path('add1', views.add1, name="add1"),
    path('add2', views.add2, name="add2"),
    path('fact1', views.fact1, name="fact1"),
    path('calculation', views.calculation, name="calculation"),
    path('viewbook/<int:p>', views.view_book, name='viewbook'),
    path('deletebook/<int:p>', views.delete_book, name='deletebook'),
    path('editbook/<int:p>', views.edit_book, name='editbook'),
    path('search/', views.search, name="search"),
    path('register/', views.register, name="register"),
    path('login/', views.user_login, name="login"),
    path('logout/', views.user_logout, name="logout"),

]
