# employee/admin.py
from django.contrib import admin
from .models import Employee

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('name', 'position', 'email', 'phone')  # Các cột hiển thị
    search_fields = ('name', 'email', 'position')  # Các trường tìm kiếm
    list_filter = ('position',)  # Lọc theo vị trí công việc

admin.site.register(Employee, EmployeeAdmin)
