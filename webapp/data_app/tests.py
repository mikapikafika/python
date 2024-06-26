import json

from django.test import TestCase, Client
from data_app.models import DataPoint


class ApiTest(TestCase):
    def setUp(self):
        self.client = Client()

    # GET tests
    def test_data_get(self):
        DataPoint.objects.create(height=1.84, weight=78.66, quality=3)
        response = self.client.get('/api/data')
        print(f'GET: {json.dumps(response.json(), indent=4)}')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()[0]['height'], 1.84)
        self.assertEqual(response.json()[0]['weight'], 78.66)
        self.assertEqual(response.json()[0]['quality'], 3)

    def test_data_get_empty(self):
        response = self.client.get('/api/data')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), [])

    # POST tests
    def test_data_post(self):
        data_point = {"height": 1.84, "weight": 78.66, "quality": 3}
        response = self.client.post('/api/data', data_point)
        print(f'POST: {json.dumps(data_point)}')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json().get('pk'), 1)

    def test_data_post_400(self):
        data_point = {"height": "", "weight": 78.66, "quality": 3}
        response = self.client.post('/api/data', data_point)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json().get('error'), 'Invalid data')

    # DELETE tests
    def test_data_delete(self):
        data_point = DataPoint.objects.create(height=1.84, weight=78.66,
                                              quality=3)
        response = self.client.delete(f'/api/data/{data_point.id}')
        print(f'DELETE: {json.dumps({"pk": data_point.pk})}')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json().get('pk'), data_point.id)
        self.assertFalse(DataPoint.objects.filter(id=data_point.id).exists())

    def test_data_delete_404(self):
        response = self.client.delete(f'/api/data/666')
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json().get('error'),
                         'Record not found')
