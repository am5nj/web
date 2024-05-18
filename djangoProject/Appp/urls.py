from django.urls import path
from Appp import views

urlpatterns = [
path('', views.index, name='index')
]