from django.contrib import admin

from .models import Catagory, Product


@admin.register(Catagory)
class CatagoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', ]
    prepopulated_fields = {
        'slug': ('name', ),
    }


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = [
        'name', 'slug', 'catagory',
        'price', 'stock', 'available', 'modified',
    ]
    list_filter = ['catagory', 'available', 'created', 'modified', ]
    list_editable = ['catagory', 'price', 'stock', 'available', ]
    search_fields = ['name', ]
    prepopulated_fields = {
        'slug': ('name', ),
    }
