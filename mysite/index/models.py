from django.db import models
from django.urls import reverse


# Create your models here.
class Info(models.Model):
    title = models.CharField(max_length=255, verbose_name='Name')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')
    content = models.TextField(blank=True, verbose_name='Opisanie')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', null=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)
    specialization = models.ForeignKey('Specialization', on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_slug': self.slug})

    class Meta:
        verbose_name = 'Информация'
        verbose_name_plural = 'Информация'
        ordering = ['-time_create', 'title']


class Contact(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name='First name')
    mail = models.CharField(max_length=100, db_index=True, verbose_name='Mail')
    message = models.TextField(blank=True, verbose_name='Message')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('contact', kwargs={'contact_id': self.pk})


class Specialization(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name='Специализация')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')

    def __str__(self):
        return self.name
    def get_absolute_url(self):
        # return reverse('specialization', kwargs={'spec_id': self.pk})
        return reverse('specialization', kwargs={'spec_slug': self.slug})

    class Meta:
        verbose_name = 'Специализация'
        verbose_name_plural = 'Специализация'
        ordering = ['id']


class News(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')
    content = models.TextField(blank=True)
    date = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=255)

    def __str__(self):
        return self.title

    # def get_absolute_url(self):
    #     return reverse('news', kwargs={'new_id': self.pk})

# <name attr>__gte = num | >=
# <name attr>__lte = num | <=


class Blog(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    time_create = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Author(models.Model):
    name = models.CharField(max_length=255)
    blog_name = models.TextField(blank=True)

    def __str__(self):
        return self.name
