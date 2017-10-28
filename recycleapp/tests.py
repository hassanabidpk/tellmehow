from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Country, Category, Material, MainComponent, MinorComponent, Product, Favorite
from .models import MainRecyclingInfomation, MinorRecyclingInfomation


class CategoryTests(APITestCase):
    def test_category_list(self):
        """
        Ensure we can get category list
        """
        # url = reverse('api/v1/category/list')
        data = {}
        response = self.client.get('http://128.199.69.81:8000/api/v1/category/list.json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class ComponentTests(APITestCase):
    def test_component_list(self):
        """
        Ensure we can get category list
        """
        response = self.client.get('http://128.199.69.81:8000/api/v1/component/list.json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


