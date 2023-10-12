from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView

from .forms import AddPostForm, AddContactForm
from .models import *


# Create your views here.
menu = [
    {'title': 'Main', 'url_name': 'home'},
    {'title': 'About', 'url_name': 'about'},
    {'title': 'Contacts', 'url_name': 'contact'},
    {'title': 'Login', 'url_name': 'login'},
    ]


# def main(request):
#     # return HttpResponse("Hello World!")
#     # return render(request, 'index/index.html')
#     posts = Info.objects.all().order_by('title')
#     # specs = Specialization.objects.all()
#     context = {
#         'title': 'Main page',
#         # 'menu': menu,
#         'posts': posts,
#         # 'specs': specs,
#         'spec_selected': 0
#     }
#     return render(request, 'index/index.html', context=context)

# Alternative for def main
    # <name app>/<name model>_list.html
class Home(ListView):
    model = Info
    template_name = 'index/index.html'
    context_object_name = 'posts'
    # extra_context = {'title': 'Main page'}

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Main page'
        context['spec_selected'] = 0
        context['menu'] = menu
        return context

    def get_queryset(self):
        return Info.objects.filter(is_published=True)


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


def contact(request, contact_id):
    # return HttpResponse('Callback')
    # contact = get_object_or_404(Info, slug=contact_slug)
    contact = get_object_or_404(Info, slug=contact_id)
    context = {
        'Name': contact.name,
        'contact': contact,
    }
    return render(request, 'index/contact.html', context=context)

def addcontact(request):
    if request.method == 'POST':
        form = AddContactForm(request.POST)
        if form.is_valid():
            # print(form.cleaned_data)
            try:
                Contact.objects.create(**form.cleaned_data)
                return redirect('home')
            except:
                form.add_error(None, 'Error while add')
    else:
        form = AddContactForm()
    context = {
        'title': 'Contact us',
        'form': form,
    }
    return render(request, 'index/addcontact.html', context=context)


def login(request):
    return HttpResponse('Login')


# def post(request, post_id):
def post(request, post_slug):
    # return HttpResponse(f'post id = {post_id}')
    post = get_object_or_404(Info, slug=post_slug)
    context = {
        'title': post.title,
        'posts': post,
        'spec_selected': post.specialization_id
    }
    return render(request, 'index/index.html', context=context)


def addpost(request):
    if request.method == 'POST':
        form = AddPostForm(request.POST, request.FILES)
        if form.is_valid():
            # print(form.cleaned_data)
            try:
                # Info.objects.create(**form.cleaned_data)
                form.save()
                return redirect('home')
            except:
                form.add_error(None, 'Error while add')
    else:
        form = AddPostForm()
    context = {
        'title': 'Add post',
        'form': form,
    }
    return render(request, 'index/addpost.html', context=context)


# def specialization(request, spec_id):
# def specialization(request, spec_slug):
#     # posts = Info.objects.all().order_by('title')
#     # posts = Info.objects.filter(specialization=spec_id)
#     posts = Info.objects.filter(specialization__slug=spec_slug)
#     if len(posts) == 0:
#         raise Http404()
#     # specs = Specialization.objects.all()
#     context = {
#         'title': 'Main page',
#         # 'menu': menu,
#         'posts': posts,
#         # 'specs': specs,
#         # 'spec_selected': spec_id
#         'spec_selected': posts[0].specialization.pk
#     }
#     return render(request, 'index/index.html', context=context)

class Specialization(ListView):
    model = Info
    template_name = 'index/index.html'
    context_object_name = 'posts'
    allow_empty = False


    # def get_context_data(self, *, object_list=None, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['title'] = 'Main page'
    #     context['spec_selected'] = context.spec_id
    #     context['menu'] = menu
    #     return context

    # def get_queryset(self):
    #     return Info.objects.filter(specialization__slug=self.kwargs['spec_slug'], is_published=True)


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