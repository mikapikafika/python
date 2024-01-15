from django.test import TestCase
from django.test import Client
import json

from data_app.models import DataPoint


class APITestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.data_point = DataPoint.objects.create(feature1=1.23,
                                                   feature2=3.45, category=1)

    def test_get_data(self):
        response = self.client.get('/api/data/')
        self.assertEqual(response.status_code, 200)

    def test_post_data(self):
        data = {'feature1': 1.23, 'feature2': 3.45, 'category': 1}
        response = self.client.post('/api/data/', data, content_type='application/json')
        self.assertEqual(response.status_code, 201)
        response_data = json.loads(response.content)
        self.assertEqual(response_data['feature1'], data['feature1'])
        self.assertEqual(response_data['feature2'], data['feature2'])
        self.assertEqual(response_data['category'], data['category'])

    def test_delete_data(self):
        response = self.client.delete(f'/api/data/{self.data_point.id}/')
        self.assertEqual(response.status_code, 200)
