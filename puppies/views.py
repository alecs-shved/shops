#from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import City, Street, CITYS, STREETS, SHOPS, Shops
from .serializers import CitySerializer, StreetSerializer, ShopsSerializer
from datetime import datetime, date, time
import random

# Create your views here.

@api_view(['GET', 'DELETE', 'PUT'])
def get_delete_update_city(request, pk):
    print('shved')
    try:
        city = City.objects.get(pk=pk)
    except City.DoesNotExist:
        #return Response(status=status.HTTP_404_NOT_FOUND)
        return Response('HTTP_400_NOT_FOUND')
    # get details of a single shops
    if request.method == 'GET':
        shopss = Shops.objects.filter()
        lis = []
        for sh in shopss:
            dic = {}
            dic['name'] = sh.name
            dic['city'] = str((City.objects.get(id=sh.street_id)).name)
            dic['street'] = str((Street.objects.get(id=sh.street_id)).name)
            dic['home'] = sh.home
            dic['time_open'] = sh.time_open
            dic['time_close'] = sh.time_close
            lis.append(dic)    
        serializer = ShopsSerializer(lis[pk-1], many=False)
        return Response(serializer.data)
        #return Response({'get':'well'})
    # delete a single puppy
    elif request.method == 'DELETE':
        return Response({'del':'well'})
    # update details of a single puppy
    elif request.method == 'PUT':
        return Response({'put':'well'})

@api_view(['GET', 'POST'])
def get_post_citys(request):
    # get all city. Pos a
    print(request)
    if request.method == 'GET':
        citys = City.objects.all()
        serializer = CitySerializer(citys, many=True)
        return Response(serializer.data)
    # insert a new record for a city
    elif request.method == 'POST':
        for cit in CITYS:
            city = City()
            city.name = cit
            city.save()
        return Response({'insert':'good'})

@api_view(['GET', 'POST'])
def get_post_street(request):
    # get all street to city. Pos b
    if request.method == 'GET':
        streets = Street.objects.filter(city_id=1)
        serializer = StreetSerializer(streets, many=True)
        return Response(serializer.data)
    # insert a new record for a street
    elif request.method == 'POST':
        citys = City.objects.all()
        for streets in STREETS:
            street = Street()
            street.name = streets
            street.city_id = citys[random.randrange(len(citys))].id
            street.save()
        return Response({'insert': 'good'})

@api_view(['GET', 'POST'])
def get_post_shop(request):
    # get all shops. not done yet  Pos d
    if request.method == 'GET':
        shopss = Shops.objects.filter()
        lis = []
        for sh in shopss:
            dic = {}
            dic['name'] = sh.name
            dic['city'] = str((City.objects.get(id=sh.street_id)).name)
            dic['street'] = str((Street.objects.get(id=sh.street_id)).name)
            dic['home'] = sh.home
            dic['time_open'] = sh.time_open
            dic['time_close'] = sh.time_close
            lis.append(dic)    
        serializer = ShopsSerializer(lis, many=True)
        return Response(serializer.data)
    # insert a new record for a shops used JSON not done yet. Pos c
    elif request.method == 'POST':
        streets = Street.objects.all()
        for shops in SHOPS:
            shop = Shops()
            shop.name = shops
            shop.street_id = streets[random.randrange(len(streets))].city_id
            shop.city = shop.street_id
            shop.home = random.randrange(29)
            shop.time_open = '8:00'
            shop.time_close = '20:00'
            shop.save()
        return Response({'insert': 'shop good'})
