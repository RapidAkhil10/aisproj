from django.shortcuts import render


def index(request):
    return render(request, 'dashboard/index.html')


def dashboard(request):
    return render(request, 'dashboard/examples/dashboard.html')


def login(request):
    return render(request, 'dashboard/examples/login.html')


def register(request):
    return render(request, 'dashboard/examples/register.html')


def icons(request):
    return render(request, 'dashboard/examples/icons.html')
