from django.urls import path
from app1 import views
app_name ="app1"
urlpatterns = [

    path('', views.home, name="home"),
    path('index/', views.index, name="index"),
]
