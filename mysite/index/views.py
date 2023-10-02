from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect
from .models import *


# Create your views here.
menu = ['Main', 'About', 'Contacts']


def main(request):
    # return HttpResponse("Hello World!")
    # return render(request, 'index/index.html')
    posts = Info.objects.all().order_by('title')
    return render(request, 'index/index.html', {'title': 'Main page', 'menu': menu, 'posts': posts})


def about(request):
    return render(request, 'index/about.html', {'title': 'About', 'menu': menu})


def category(request, catid):
    # if request.POST:
    #     print(request.POST)
    # if request.GET:
    #     print(request.GET)
    return HttpResponse(f"<h1>Category {catid}</h1>")


def archive(request, year):
    if(int(year) > 2022):
        # raise Http404()
        # return redirect('/index', permanent=True)
        return redirect('home', permanent=True)
    return HttpResponse(f"<h1>Archive {year}</h1>")


def pageNotFound(request, exception):
    return HttpResponseNotFound(f"<h1>Page not found!</h1>")