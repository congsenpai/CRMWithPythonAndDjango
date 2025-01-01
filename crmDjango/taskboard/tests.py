from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient
from employee.models import Employee
from .models import Task


class TaskAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()

        # Create a test employee
        self.employee = Employee.objects.create(
            name="Jane Doe",
            position="Developer",
            email="jane.doe@example.com",
            phone="1234567890",
            address="123 Developer St",
        )

        # Create initial task data
        self.task_data = {
            "title": "Test Task",
            "description": "This is a test task.",
            "status": Task.Status.NOT_COMPLETED,
            "assigned_to": self.employee.pk,
        }

        # Create a test task
        self.task = Task.objects.create(
            title="Existing Task",
            description="This is an existing task.",
            status=Task.Status.NOT_COMPLETED,
            assigned_to=self.employee,
        )

        # Define the base URL for the Task API
        self.url = "/api/taskboards/"

    def test_create_task(self):
        response = self.client.post(self.url, self.task_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        response_data = response.json()
        self.assertEqual(response_data["title"], self.task_data["title"])
        self.assertEqual(response_data["status"], self.task_data["status"])
        self.assertEqual(response_data["assigned_to"], self.employee.pk)


    def test_get_all_tasks(self):
        Task.objects.create(
            title="Second Task",
            description="This is another test task.",
            status=Task.Status.NOT_COMPLETED,
            assigned_to=self.employee,
        )
        response = self.client.get(self.url, format="json")
        print(response.json())  # Debug response
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.json()), 2)

    def test_get_single_task(self):
        response = self.client.get(f"{self.url}{self.task.pk}/", format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response_data = response.json()
        self.assertEqual(response_data["title"], self.task.title)
        self.assertEqual(response_data["description"], self.task.description)

    def test_update_task(self):
        updated_data = {
            "title": "Updated Task",
            "description": "This is an updated task description.",
            "status": Task.Status.COMPLETED,
            "assigned_to": self.employee.pk,
        }
        response = self.client.put(
            f"{self.url}{self.task.pk}/", updated_data, format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response_data = response.json()
        self.assertEqual(response_data["title"], updated_data["title"])
        self.assertEqual(response_data["status"], updated_data["status"])

    def test_delete_task(self):
        response = self.client.delete(f"{self.url}{self.task.pk}/", format="json")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Task.objects.filter(id=self.task.pk).exists())
