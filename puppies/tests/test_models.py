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

'''class StreetTest(TestCase):
    """ Test module for Street model """
    def setUp(self):

        City.objects.create(
            name='Kap',)

        Street.objects.create(
            name='Tagan',
            city_id=1 ,
            )
          
    def test_street(self):
        street_tagan = Street.objects.get(name='Tagan')
        #street_turmal = Street.objects.get(name='Turmal')
        self.assertEqual(
            street_tagan.get_breed(), "Tagan belongs to ")
        #self.assertEqual(
         #   street_turmal.get_breed(), "Turmal belongs to ")'''
