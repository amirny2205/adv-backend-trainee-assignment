from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from ads.models import Ad

client = APIClient()


class AdTests(APITestCase):

    def setUp(self):
        self.obj = Ad.objects.create(title='title', price=100, photos=['one', 'two'])

    def test_listview(self):
        response = client.get(reverse('ad-list'))
        self.assertEqual(response.status_code, 200)

    def test_detailview(self):
        response = client.get(reverse('ad-detail', kwargs={'pk':self.obj.id}))
        self.assertEqual(response.status_code, 200)

    def test_create(self):
        response = client.post(reverse('ad-create'),
                               {'title': 'title 01', 'description': 'description01', 'photos': '["one","two"]',
                                'price': 300})
        self.assertEqual(response.status_code, 201)

    def test_main_photo(self):
        response = client.get(reverse('ad-detail', kwargs={'pk':self.obj.id}))
        self.assertContains(response, 'main_photo')

    def test_fields(self):
        response = client.get(reverse('ad-detail', kwargs={'pk':self.obj.id}) + '?fields=photos,description')
        self.assertContains(response, 'photos')
        self.assertContains(response, 'description')

    def test_title_validator(self):
        response = client.post(reverse('ad-create'),
                               {'title': "s"*201, 'description': 'description01', 'photos': '["one","two"]',
                                'price': 300})
        self.assertEqual(response.status_code, 400)

    def test_description_validator(self):
        response = client.post(reverse('ad-create'),
                               {'title': "title", 'description': "s"*1001, 'photos': '["one","two"]',
                                'price': 300})
        self.assertEqual(response.status_code, 400)

    def test_photos_validator(self):
        response = client.post('/ad_create/',
                               {'title': "title", 'description': "description",
                                'photos': '["one","two","three","four"]',
                                'price': 300})
        self.assertEqual(response.status_code, 400)
