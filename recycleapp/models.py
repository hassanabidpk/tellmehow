# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
import datetime
from django.utils import timezone
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
from django.template.defaultfilters import slugify

class Country(models.Model):
    name = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Countries"
    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=250)
    slug = models.SlugField(max_length=100, unique=True, allow_unicode=True)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Categories"
    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.name)
        return super(Category, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class Material(models.Model):
    name = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Component(models.Model):
    name = models.CharField(max_length=250)
    type = models.CharField(max_length=100)
    category = models.ForeignKey(Category,
                            models.SET_NULL,
                            blank=True,
                            null=True,)
    material = models.ForeignKey(Material, on_delete=models.CASCADE)
    main_component = models.ForeignKey('self',
                            models.SET_NULL,
                            blank=True,
                            null=True,)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    code = models.CharField(max_length=100)
    name = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, allow_unicode=True)
    search_keywords = models.CharField(max_length=250)
    main_component = models.ForeignKey(Component, on_delete=models.CASCADE)
    writer = models.ForeignKey(User)
    photo = models.ImageField(upload_to="product_images/", null=True, blank=True)
    photo_thumbnail = ImageSpecField(source='photo',
                                       processors=[ResizeToFill(360, 225)],
                                       format='JPEG',
                                       options={'quality': 90})
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.name)
        return super(Product, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class RecyclingInfomation(models.Model):
    info = models.TextField()
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    component = models.ForeignKey(Component, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Recycle Infos"

    def __str__(self):
        return self.country.name + ' - ' + self.component.name


class Favorite(models.Model):
    user = models.ForeignKey(User)
    recycling_info = models.ForeignKey(RecyclingInfomation, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{} - {}".format(self.user, "info")
