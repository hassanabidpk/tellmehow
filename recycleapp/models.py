# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
import datetime
from django.utils import timezone
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
from django.template.defaultfilters import slugify
import json

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

class MinorComponent(models.Model):
    name = models.CharField(max_length=250)
    material = models.ForeignKey(Material, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
        
class MainComponent(models.Model):
    name = models.CharField(max_length=250)
    category = models.ForeignKey(Category,
                            models.SET_NULL,
                            blank=True,
                            null=True,)
    material = models.ForeignKey(Material, on_delete=models.CASCADE)
    minor_components = models.ManyToManyField(MinorComponent, null=True, blank=True)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    code = models.CharField(max_length=100, null=True)
    name = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, allow_unicode=True)
    search_keywords = models.CharField(max_length=250)
    main_component = models.ForeignKey(MainComponent, on_delete=models.CASCADE)
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


class MainRecyclingInfomation(models.Model):
    info = models.TextField()
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    component = models.ForeignKey(MainComponent, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Main Recycle Infos"

    def __str__(self):
        return "info"

class MinorRecyclingInfomation(models.Model):
    info = models.TextField()
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    component = models.ForeignKey(MinorComponent, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Minor Recycle Infos"

    def __str__(self):
        return self.country.name + ' - ' + self.component.name


class Favorite(models.Model):
    user = models.ForeignKey(User)
    recycling_info = models.ForeignKey(MainRecyclingInfomation, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{} - {}".format(self.user, "info")
