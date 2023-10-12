from django.urls import path, re_path
from .views import *


urlpatterns = [
    # path('', main),
    # path('category/', category),
    # path('category/<int:catid>', category),
    # path('category/<slug:catid>', category),
    # re_path(r'archive/(?P<year>[0-9]{4})/', archive),

    # path('', main, name='home'),
    path('', Home.as_view(), name='home'),

    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    # path('contact/<slug:contact_slug>', contact, name='contact'),
    path('addcontact/addcontact', addcontact, name='addcontact'),
    path('login/', login, name='login'),
    path('post/<slug:post_slug>/', post, name='post'),
    path('addpost/addpost/', addpost, name='addpost'),

    # path('specialization/<int:spec_id>/', specialization, name='specialization'),
    # path('specialization/<slug:spec_slug>/', specialization, name='specialization'),
    path('specialization/<slug:spec_slug>/', Specialization.as_view(), name='specialization'),

    path('news/', news, name='news'),
]