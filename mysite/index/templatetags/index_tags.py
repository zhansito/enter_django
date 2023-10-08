from django import template
from index.models import *
from index.views import *

register = template.Library()

@register.simple_tag(name='getspecs')
def get_specializations(filter=None):
    if not filter:
        return Specialization.objects.all()
    else:
        return Specialization.objects.filter(pk=filter)


@register.inclusion_tag('index/list_specializations.html')
def show_specializations(sort=None, spec_selected=0):
    if not sort:
        specs = Specialization.objects.all()
    else:
        specs = Specialization.objects.order_by(sort)
    return {'specs': specs, 'spec_selected': spec_selected}
@register.inclusion_tag('index/news.html')
def show_news(sort=None, news_selected=0):
    if not sort:
        news = News.objects.all()
    else:
        news = News.objects.order_by(sort)
    return {'news': news, 'news_selected': news_selected}

# my variant
# @register.inclusion_tag('index/list_menu.html')
# def show_menu():
#     menu_items = menu
#     return {'menu': menu_items}

@register.inclusion_tag('index/header.html')
def show_header():
    menu = [
        {'title': 'Main', 'url_name': 'home'},
        {'title': 'About', 'url_name': 'about'},
        {'title': 'Contacts', 'url_name': 'contact'},
        {'title': 'News', 'url_name': 'news'},
        {'title': 'Login', 'url_name': 'login'},
    ]
    return {'menu': menu}


@register.inclusion_tag('index/footer.html')
def show_footer():
    menu = [
        {'title': 'Main', 'url_name': 'home'},
        {'title': 'About', 'url_name': 'about'},
        {'title': 'Contacts', 'url_name': 'contact'},
        {'title': 'News', 'url_name': 'news'},
        {'title': 'Login', 'url_name': 'login'},
    ]
    return {'menu': menu}


