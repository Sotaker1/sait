from django.shortcuts import render

def index(request):
    return render(request,'main/shapka.html')


def about(request):
    return render(request,'main/about.html')

def obrawenie(request):
    return render(request,'main/obrawenie.html')
