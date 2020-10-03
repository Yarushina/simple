from django.shortcuts import render


def index(request):
    return render(request, "index.html")

def about_us(request):
    return render(request, "about_us.html")

def work(request):
    return render(request, "work.html")