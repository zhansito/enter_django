from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, get_object_or_404
from .models import *


# Create your views here.
menu = [
    {'title': 'Main', 'url_name': 'home'},
    {'title': 'About', 'url_name': 'about'},
    {'title': 'Contacts', 'url_name': 'contact'},
    {'title': 'Login', 'url_name': 'login'},
    ]


def main(request):
    # return HttpResponse("Hello World!")
    # return render(request, 'index/index.html')
    posts = Info.objects.all().order_by('title')
    # specs = Specialization.objects.all()
    context = {
        'title': 'Main page',
        # 'menu': menu,
        'posts': posts,
        # 'specs': specs,
        'spec_selected': 0
    }
    return render(request, 'index/index.html', context=context)


def news(request):
    news = News.objects.all()
    context = {
        'title': 'News',
        'news': news,
        'news_selected': 0
    }
    return render(request, 'index/news.html', context=context)


def about(request):
    context = {'title': 'About', 'menu': menu}
    return render(request, 'index/about.html', context=context)


def contact(request):
    return HttpResponse('Callback')


def login(request):
    return HttpResponse('Login')


def post(request, post_id):
    # return HttpResponse(f'post id = {post_id}')
    post = get_object_or_404(Info, pk=post_id)
    context = {
        'title': post.title,
        'posts': post,
        'spec_selected': post.specialization_id
    }
    return render(request, 'index/index.html', context=context)


def specialization(request, spec_id):
    # posts = Info.objects.all().order_by('title')
    posts = Info.objects.filter(specialization=spec_id)
    if len(posts) == 0:
        raise Http404()
    # specs = Specialization.objects.all()
    context = {
        'title': 'Main page',
        # 'menu': menu,
        'posts': posts,
        # 'specs': specs,
        'spec_selected': spec_id
    }
    return render(request, 'index/index.html', context=context)


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