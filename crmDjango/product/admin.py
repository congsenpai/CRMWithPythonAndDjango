# product/admin.py
from django.contrib import admin
from .models import Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock', 'created_at')  # Các cột hiển thị
    search_fields = ('name',)  # Trường tìm kiếm theo tên sản phẩm
    list_filter = ('created_at',)  # Lọc theo ngày tạo sản phẩm

admin.site.register(Product, ProductAdmin)
