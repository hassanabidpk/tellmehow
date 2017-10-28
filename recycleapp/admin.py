from django.contrib import admin
from .models import Country, Category, Material, MainComponent, MinorComponent, Product, Favorite
from .models import MainRecyclingInfomation, MinorRecyclingInfomation

class ProductAdmin(admin.ModelAdmin):
    exclude = ('slug',)

class CategoryAdmin(admin.ModelAdmin):
    exclude = ('slug',)

admin.site.register(Country)
admin.site.register(Product, ProductAdmin)
admin.site.register(MainRecyclingInfomation)
admin.site.register(MinorRecyclingInfomation)
admin.site.register(Material)
admin.site.register(MainComponent)
admin.site.register(MinorComponent)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Favorite)