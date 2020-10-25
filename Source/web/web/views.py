from django.shortcuts import render


def index(request):
    return render(request, 'indext.html')


def report(request):
    return render(request, 'report.html')