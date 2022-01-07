from django.urls import path
from . import views

urlpatterns = [
    #paths core
    path('', views.home, name="admindashboard"),
]