from django.test import TestCase, Client


class ApiTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_api_data_post(self):
        data = {"feature1": 1.23, "feature2": 1.88,
                "category": 1}
        response = self.client.post('/api/data', data)
        print(response.json())

        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json().get('pk'), 1)

    def test_api_data_post_invalid_data(self):
        data = {"feature1": 1.23, "feature2": 1.88,
                "category": ""}
        response = self.client.post('/api/data', data)

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json().get('error'), 'Invalid data')

    def test_api_data_get_empty(self):
        response = self.client.get('/api/data')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), [])

    def test_api_data_get(self):
        data = {"feature1": 1.23, "feature2": 1.88,
                "category": 1}
        self.client.post('/api/data', data)

        response = self.client.get('/api/data')
        self.assertEqual(response.status_code, 200)
        self.assertNotEquals(response.json(), [])

    def test_api_data_get_with_data(self):
        data = {"feature1": 1.23, "feature2": 1.88,
                "category": 1}
        self.client.post('/api/data', data)
        response = self.client.get('/api/data')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), [
            {'id': 1, 'feature1': 1.23, 'feature2': 1.88,
             'category': 1}])
