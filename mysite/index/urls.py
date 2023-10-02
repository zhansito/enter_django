from django.urls import path, re_path
from .views import *


urlpatterns = [
    # path('', main),
    # path('category/', category),
    # path('category/<int:catid>', category),
    # path('category/<slug:catid>', category),
    # re_path(r'archive/(?P<year>[0-9]{4})/', archive),
    path('', main, name='home'),
    path('about/', about, name='about'),
]