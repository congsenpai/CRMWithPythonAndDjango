# customer/admin.py
from django.contrib import admin
from .models import Customer

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'address', 'age')  # Cột hiển thị trên trang danh sách
    search_fields = ('name', 'email')  # Cột để tìm kiếm
    list_filter = ('age',)  # Cột lọc dữ liệu (ở đây là lọc theo độ tuổi)

admin.site.register(Customer, CustomerAdmin)
