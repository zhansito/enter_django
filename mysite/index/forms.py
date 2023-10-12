from django import forms
from django.core.exceptions import ValidationError

from .models import *


class AddPostForm(forms.ModelForm):
    # title = forms.CharField(max_length=255, label='Zagolovok', widget=forms.TextInput(attrs={'class': 'form__input'}))
    # slug = forms.SlugField(max_length=255, label='URL')
    # content = forms.CharField(widget=forms.Textarea(attrs={'cols': 60, 'rows': 10}), label='Content', required=False)
    # is_published = forms.BooleanField(label='Publish', initial=True)
    # specialization = forms.ModelChoiceField(queryset=Specialization.objects.all(), label='Specializaciya', empty_label='Choose specialization')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['specialization'].empty_label = 'Choose the specialization'

    class Meta:
        model = Info
        # fieds = '__all__'
        fields = ['title', 'slug', 'content', 'is_published', 'specialization', 'photo']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form__input'}),
            # 'content': forms.Textarea(attrs={'cols': 60, 'rows': 10})
            'content': forms.Textarea(attrs={'class': 'form__text'})
        }

    def clean_title(self):
        title = self.cleaned_data['title']
        if len(title)>20:
            raise ValidationError('Length exceeded 20 symbols')
        return title


class AddContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'mail', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form__input'}),
            'mail': forms.TextInput(attrs={'class': 'form__input'}),
            'message': forms.Textarea(attrs={'cols': 60, 'rows': 10})
        }

# class AddContactForm(forms.Form):
#     name = forms.CharField(max_length=255, label='First name', widget=forms.TextInput(attrs={'class': 'form__input'}))
#     mail = forms.CharField(max_length=255, label='Mail', widget=forms.TextInput(attrs={'class': 'form__input'}))
#     message = forms.CharField(widget=forms.Textarea(attrs={'cols': 60, 'rows': 10}), label='Message', required=True)
