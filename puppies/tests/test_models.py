from django.test import TestCase
from ..models import City, Street, Shops

class CityTest(TestCase):
    """ Test module for City model """

    def setUp(self):
        City.objects.create(
            name='Kap',)
        City.objects.create(
            name='Aral',)

    def test_city(self):
        city_casper = City.objects.get(name='Kap')
        city_muffin = City.objects.get(name='Aral')
        self.assertEqual(
            city_casper.get_breed(), "Kap belongs to ")
        self.assertEqual(
            city_muffin.get_breed(), "Aral belongs to ")

