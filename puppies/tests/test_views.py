import json
from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse
from ..models import City, Street
from ..serializers import CitySerializer

# initialize the APIClient app

client = Client()

class GetAllCityTest(TestCase):
    """ Test module for GET all puppies API """
    def setUp(self):
        City.objects.create(
            name='Casper',)
        City.objects.create(
            name='Muffin',)
        City.objects.create(
            name='Rambo',)
        City.objects.create(
            name='Ricky',)
    def test_get_all_puppies(self):
        # get API response
        response = client.get(reverse('get_post_citys'))
        # get data from db
        puppies = City.objects.all()
        serializer = CitySerializer(puppies, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

'''class GetAllStreetTest(TestCase):
    """ Test module for GET all puppies API """
    def setUp(self):
        City.objects.create(
            name='Casper',)
        Street.objects.create(
            name='Casper', city_id=1)
    def test_get_all_puppies(self):
        # get API response
        response = client.get(reverse('get_post_street'))
        print('shved')
        # get data from db
        puppies = Street.objects.all()
        serializer = StreetSerializer(puppies, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)'''