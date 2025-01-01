from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient
from customer.models import Customer

class CustomerAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.customer_data = {
            "name": "John Doe",
            "email": "john.doe@example.com",
            "phone": "1234567890",
            "address": "123 Main St",
            "age": 30
        }
        self.customer = Customer.objects.create(**self.customer_data)
        self.url = '/api/customers/'

    def test_create_customer(self):
        response = self.client.post(self.url, self.customer_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        response_data = response.json()  # Safely parse JSON response
        self.assertEqual(response_data['name'], self.customer_data['name'])
        self.assertEqual(response_data['email'], self.customer_data['email'])

    def test_get_all_customers(self):
        response = self.client.get(self.url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        response_data = response.json()
        self.assertEqual(len(response_data), 1)
        self.assertEqual(response_data[0]['name'], self.customer.name)

    def test_get_single_customer(self):
        response = self.client.get(f"{self.url}{self.customer.pk}/", format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        response_data = response.json()
        self.assertEqual(response_data['name'], self.customer.name)
        self.assertEqual(response_data['email'], self.customer.email)

    def test_update_customer(self):
        updated_data = {
            "name": "John Updated",
            "email": "john.updated@example.com",
            "phone": "0987654321",
            "address": "456 Updated St",
            "age": 35
        }
        response = self.client.put(f"{self.url}{self.customer.pk}/", updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        response_data = response.json()
        self.assertEqual(response_data['name'], updated_data['name'])
        self.assertEqual(response_data['email'], updated_data['email'])

        # Validate changes in the database
        self.customer.refresh_from_db()
        self.assertEqual(self.customer.name, updated_data['name'])
        self.assertEqual(self.customer.email, updated_data['email'])

    def test_delete_customer(self):
        response = self.client.delete(f"{self.url}{self.customer.pk}/", format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        # Confirm deletion in the database
        with self.assertRaises(Customer.DoesNotExist):
            Customer.objects.get(id=self.customer.pk)
