from django.contrib import admin
from .models import Category, Product


class CateAd(admin.ModelAdmin):
    list_display = ['name', 'slug', ]
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Category, CateAd)


class ProAd(admin.ModelAdmin):
    list_display = ['name', 'price', 'stock', 'available', 'created', 'updated',]
    list_editable = ['price', 'stock', 'available']
    list_per_page = 20
    prepopulated_fields = {'slug': ('name', )}


admin.site.register(Product, ProAd)
