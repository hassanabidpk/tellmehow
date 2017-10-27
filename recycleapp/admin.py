from django.contrib import admin
from .models import Country, Category, Material, Component, Product, RecyclingInfomation, Favorite

class ProductAdmin(admin.ModelAdmin):
    exclude = ('slug',)

class CategoryAdmin(admin.ModelAdmin):
    exclude = ('slug',)

admin.site.register(Country)
admin.site.register(Product, ProductAdmin)
admin.site.register(RecyclingInfomation)
admin.site.register(Material)
admin.site.register(Component)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Favorite)