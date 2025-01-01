from django.db import models
from employee.models import Employee

class Task(models.Model):
    class Status(models.TextChoices):
        COMPLETED = 'completed', 'Đã hoàn thành'
        NOT_COMPLETED = 'not_completed', 'Chưa hoàn thành'

    title = models.CharField(max_length=100)
    description = models.TextField()
    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.NOT_COMPLETED,
    )
    assigned_to = models.ForeignKey(Employee, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
