from django.shortcuts import render


def file_list(request):
    return render(request, "file_list.html")


def github(request):
    return render(request, "github.html")


def about(request):
    return render(request, "about.html")
