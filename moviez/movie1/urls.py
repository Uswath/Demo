"""
URL configuration for moviez project.

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
from movie1 import views

app_name = "movie1"

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('',views.home,name='home'),
    path('', views.MovieListView.as_view(), name='home'),

    # path('view/<int:pk>',views.view,name='view'),
    path('view/<int:pk>', views.MoviedetailView.as_view(), name='view'),

    # path('update/<int:p>', views.update, name='update'),
    path('update/<int:pk>', views.Movieupdateview.as_view(), name='update'),

    # path('delete/<int:p>', views.delete, name='delete'),
    path('delete/<int:pk>', views.Moviedelete.as_view(), name='delete'),

    # path('add/', views.add, name='add')
    path('add/', views.Movieaddview.as_view(), name='add'),


]
