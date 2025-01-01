# taskboard/admin.py
from django.contrib import admin
from .models import Task

class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'assigned_to', 'status', 'created_at')
    list_display_links = ('title',)  # Chỉ cho phép nhấp vào "title" để chỉnh sửa
    search_fields = ('title', 'assigned_to__name')
    list_filter = ('status', 'assigned_to')

    def assigned_to(self, obj):
        return obj.assigned_to.name

    assigned_to.admin_order_field = 'assigned_to'
    assigned_to.short_description = 'Employee Name'

admin.site.register(Task, TaskAdmin)
