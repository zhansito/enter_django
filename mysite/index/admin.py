from django.contrib import admin
from .models import *

# Register your models here.


class InfoAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'time_create', 'photo', 'is_published')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')


class SpecializationAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('title', )


admin.site.register(Info, InfoAdmin)
admin.site.register(Specialization, SpecializationAdmin)