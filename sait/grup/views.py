from django.shortcuts import render
from .models import grupa


def grup_home(request):
    grup = grupa.objects.all()
    return render(request, 'grup/grup_home.html', {'grup':grup})
