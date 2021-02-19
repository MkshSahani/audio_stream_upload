from django.urls import path
from . import views
urlpatterns = [
    path('', views.homePage, name="Home Page"),
    path('mon', views.dummy, name="dummy"),
]
