import json
from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse
from ..models import City, Street
from ..serializers import CitySerializer

# initialize the APIClient app

client = Client()

class GetAllCityTest(TestCase):
    """ Test module for GET all city API """
    def setUp(self):
        City.objects.create(
            name='Kupustin-Yar',)
        City.objects.create(
            name='Astrahan',)
    def test_get_post_citys(self):
        # get API response
        response = client.get(reverse('get_post_citys'))
        # get data from db
        citys = City.objects.filter(name='Kupustin-Yar')
        serializer = CitySerializer(citys, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class CreateNewCityTest(TestCase):
    """ Test module for inserting a new city """
    def setUp(self):
        self.valid_payload = {
            'name': 'Kupustin-Yar',
        }
        self.invalid_payload = {
            'name': '',
        }
    def test_create_valid_city(self):
        response = client.post(
            reverse('get_post_citys'),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    def test_create_invalid_puppy(self):
        response = client.post(
            reverse('get_post_citys'),
            data=json.dumps(self.invalid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)