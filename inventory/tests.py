from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import Item  # Import your model
import random
import string


class ItemModelTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user_data = {
            "username": "testuser",
            "password": "testpassword"
        }
        # Register a test user
        self.client.post(reverse('register'), self.user_data)
        # Log in to get the token
        login_response = self.client.post(reverse('login'), {
            "username": self.user_data["username"],
            "password": self.user_data["password"]
        })
        self.token = login_response.data['access']
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.token}')

        self.item_data = {
            "name": "Test Item",
            "description": "Test Description",
            "quantity": 10,
            "price": "100.00"
        }
        self.item = Item.objects.create(**self.item_data)

    def test_item_creation(self):
        self.assertEqual(self.item.name, "Test Item")
        self.assertEqual(self.item.description, "Test Description")
        self.assertEqual(self.item.quantity, 10)
        self.assertEqual(str(self.item.price), "100.00")

    def test_item_str_representation(self):
        self.assertEqual(str(self.item), self.item.name)

    def generate_random_name(self, length=10):
        return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

    def test_create_item(self):
        url = reverse('item-create')
        new_item_data = {
            "name": self.generate_random_name(),
            "description": "New Description",
            "quantity": 5,
            "price": "50.00"
        }
        response = self.client.post(url, new_item_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Item.objects.count(), 2)  # Since one item was created in setUp

    def test_update_item(self):
        url = reverse('item-detail', kwargs={'pk': self.item.pk})
        updated_data = {
            "name": "Updated Test Item",
            "description": "Updated Description",
            "quantity": 20,
            "price": "150.00"
        }
        response = self.client.put(url, updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Refresh the item from the database
        self.item.refresh_from_db()
        self.assertEqual(self.item.name, "Updated Test Item")
        self.assertEqual(self.item.description, "Updated Description")
        self.assertEqual(self.item.quantity, 20)
        self.assertEqual(str(self.item.price), "150.00")

    def test_get_item(self):
        url = reverse('item-detail', kwargs={'pk': self.item.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], self.item.name)
        self.assertEqual(response.data['description'], self.item.description)
        self.assertEqual(response.data['quantity'], self.item.quantity)
        self.assertEqual(response.data['price'], str(self.item.price))

    def test_delete_item(self):
        url = reverse('item-detail', kwargs={'pk': self.item.pk})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Item.objects.count(), 0)  # Ensure item is deleted
