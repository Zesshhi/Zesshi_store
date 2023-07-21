from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

'''
Genre
========
title, slug

Platform
=========
title, slug

Posts
========
title, slug, content, photo, views, price, genre, platform

'''


class Genre(models.Model):
    title = models.CharField(max_length=255, verbose_name='Жанр')
    slug = models.SlugField(max_length=255, verbose_name='Url', unique=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('genre', kwargs={'slug': self.slug})

    class Meta:
        ordering = ['title']
        verbose_name = 'Жанр'
        verbose_name_plural= 'Жанры'


class Platform(models.Model):
    title = models.CharField(max_length=255, verbose_name='Платформа')
    slug = models.SlugField(max_length=255, verbose_name='Url', unique=True)

    def __str__(self):
        return self.title


    def get_absolute_url(self):
        return reverse('platform', kwargs={'slug': self.slug})


    class Meta:
        ordering = ['title']
        verbose_name = 'Платформа'
        verbose_name_plural= 'Платформы'


class Posts(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название игры')
    slug = models.SlugField(max_length=255, verbose_name='Url', unique=True)
    description = models.TextField(blank=True, verbose_name='Описание')
    content = models.TextField(blank=True, verbose_name='Контент')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True, verbose_name='Фото')
    views = models.IntegerField(default=0, verbose_name='Количество просмотров')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
    genre = models.ManyToManyField(Genre, blank=True, related_name='posts')
    platform = models.ManyToManyField(Platform, blank=True, related_name='posts')
    available = models.BooleanField(default=True, verbose_name ='Наличие')
    version_of_platform = models.CharField(max_length=55, verbose_name='Версия для label', default='PS4')
    release_date = models.DateTimeField(default='2023-01-01')


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={'slug': self.slug})


    class Meta:
        ordering = ['title']
        index_together = (('id', 'slug'),)
        verbose_name = 'Пост'
        verbose_name_plural= 'Посты'


class Carousel(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    slug = models.SlugField(max_length=255, verbose_name='Url', unique=True)
    photo = models.ImageField(upload_to='photos/carousel/%Y/%m/%d/')

    class Meta:
        ordering = ['title']
        verbose_name = 'Главная слайдер'
        verbose_name_plural = 'Слайдеры'

    def __str__(self):
        return self.title


class Order(models.Model):
    username = models.CharField(max_length=50, verbose_name='Имя пользователя')
    email = models.EmailField()
    vk_or_telegram = models.CharField(max_length=255, verbose_name='Ссылка для связи', default='vk.com')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    paid = models.BooleanField(default=False, verbose_name='Оплачено')


    class Meta:
        ordering = ['-created',]
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'


    def __str__(self):
        return 'Заказ {}'.format(self.id)


    def get_cost(self):
        return sum(item.get_cost() for item in self.items.all())


    def get_total_price(self):
        return sum(products.price for products in OrderItem.objects.filter(order=self.id))



class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='order', on_delete=models.CASCADE)
    product = models.ForeignKey(Posts, related_name='order_items', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return '{}'.format(self.id)

    def get_cost(self):
        return self.price


