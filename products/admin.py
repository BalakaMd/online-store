from django.contrib import admin

from products.models import Basket, Products, ProductsCategory

admin.site.register(ProductsCategory)


@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'quantity', 'display_categories')

    def display_categories(self, obj):
        return ", ".join([category.name for category in obj.category.all()])

    display_categories.short_description = 'Categories'

    search_fields = ('name',)


class BasketAdmin(admin.TabularInline):
    model = Basket
    readonly_fields = ('products', 'quantity')
    extra = 0
