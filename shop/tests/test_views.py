import json
from rest_framework.response import Response
from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse
from ..models import City, Street, Shops
from ..serializers import CitySerializer, StreetSerializer, ShopsallSerializer 

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
        citys = City.objects.filter()
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

    def test_create_invalid_city(self):
        response = client.post(
            reverse('get_post_citys'),
            data=json.dumps(self.invalid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class GetAllstreetTest(TestCase):
    """ Test module for GET all street API """
    def setUp(self):
        city = City.objects.create(
            name='Kupustin-Yar',)
        idu = City.objects.get(name='Kupustin-Yar').id
        Street.objects.create(name='Malina-street', city_id=idu)

    def test_get_post_streets(self):
        # get API response
        response = client.get(reverse('get_post_street'))
        # get data from db
        street = Street.objects.filter()
        serializer = StreetSerializer(street, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class GetAllshopsTest(TestCase):
    """ Test module for GET all shops API """
    def setUp(self):
        city = City.objects.create(
            name='Kupustin-Yar',)
        street = Street.objects.create(name='Malina-street', city_id=city.id)
        Shops.objects.create(
            name='Shop-one', city_id=city.id, street_id=street.id, home=14, time_open='08:00', time_close='20:00')
        
    def test_get_post_shops(self):
        # get API response
        # get data from db
        url_list = [
        '/shop/?street=Malina-street&city=Kupustin-Yar&open=1'
        ]
        response = client.get(url_list[0])
        shops = filter(lambda x: x.open == True, Shops.objects.filter(city__name="Kupustin-Yar", street__name="Malina-street"))
        serializer = ShopsallSerializer(shops, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)