from django.urls import path
from . import views

urlpatterns = [
    path('', views.grup_home, name='grup_home')
]