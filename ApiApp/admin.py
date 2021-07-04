from django.contrib import admin
from .models import Category, Book, Product, Cart

admin.site.site_header = 'E-commerce'


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    search_fields = ('title',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category', 'product_tag',
                    'price', 'stock', 'created_by')
    search_fields = ('name',)
    list_filter = (
        'category',
    )


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category', 'date_created', 'stock')
    search_fields = ('title',)
    list_filter = (
        'status', 'category__title', 'date_created'
    )

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ('cart_id', 'created_at')
    search_fields = ('cart_id',)


