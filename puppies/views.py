#from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import City, Street, CITYS, STREETS, SHOPS, Shops
from django.db.models import Q
from .serializers import CitySerializer, StreetSerializer, ShopsSerializer, ShopsallSerializer
from datetime import datetime, date, time
from django.db.models import Avg
from django.db.models import Count
import json
#from datetime import datetime
import time
import random

# Create your views here.

@api_view(['GET', 'POST'])
def get_post_citys(request):
    #query = request.GET.get("q")
    # get all city. Pos a
    #curl  -v -X GET -H "Content-Type: application/json"  http://127.0.0.1:8000/city/
    if request.method == 'GET':
        citys = City.objects.filter(name='Kupustin-Yar')
        serializer = CitySerializer(citys, many=True)
        return Response(serializer.data)
    # insert a new record for a city
    #curl  -v -X POST --data '{"name": "Kupustin-Yar"}' -H "Content-Type: application/json"  http://127.0.0.1:8000/city/
    elif request.method == 'POST':
        data = {
           'name': request.data.get('name')
        }
        serializer = CitySerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def get_post_street(request):
    # get all street to city. Pos b
    # curl  -v -X GET -H "Content-Type: application/json"  http://127.0.0.1:8000/city/street/
    if request.method == 'GET':
        streets = Street.objects.filter(city_id=2)
        serializer = StreetSerializer(streets, many=True)
        return Response(serializer.data)
    # insert a new record for a street
    #curl  -v -X POST --data '{"name":"Malina-street","city":3}' -H "Content-Type: application/json"  http://127.0.0.1:8000/city/street/
    elif request.method == 'POST':
        data = {
           'name': request.data.get('name'),
           'city': request.data.get('city'),
        }
        serializer = StreetSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def get_post_shop(request):
    # get all street to city. Pos c
    # curl  -v -X GET -H "Content-Type: application/json"  http://127.0.0.1:8000/shop/
    # curl  -v -X GET --data '{"name":"shop-six", "city": "Volgograd", "street":"Sudovaya-street"}' -H "Content-Type: application/json"  http://127.0.0.1:8000/shop/
    if request.method == 'GET':
        data = {
           'name': request.data.get('name'),
           'city': request.data.get('city'),
           'street': request.data.get('street'),
        }
        if data['city'] is not None:
            city = City.objects.filter(name=data['city']).values()
            data['city'] = city[0]['id']
            if data['street'] is not None:
                data['street'] = city[0]['id']
        datar = {}
        for dt in data:
            if data[dt] is not None:
                 datar[dt] = data[dt]     
        shop = Shops.objects.filter(**datar)
        lis = []
        for sh in shop:
            dic = {}
            dic['id'] = sh.id
            dic['name'] = sh.name
            dic['city'] = City.objects.get(id=sh.street_id)
            dic['street'] = Street.objects.get(id=sh.street_id)
            dic['home'] = sh.home
            dic['time_open'] = sh.time_open
            dic['time_close'] = sh.time_close
            now = datetime.now()
            d = date.today()
            open = datetime.strptime(str(d) + ' ' + sh.time_open, "%Y-%m-%d %H:%M")
            close = datetime.strptime(str(d) + ' ' + sh.time_close, "%Y-%m-%d %H:%M")
            if now > open and now < close:
                dic['open'] = 1
            else:
                dic['open'] = 0
            lis.append(dic)
        serializer = ShopsallSerializer(lis, many=True)
        return Response(serializer.data)
    # insert a new record for a street
    #curl  -v -X POST --data '{"name":"shop-six","city":2, "street":2, "home":14, "time_open":"8:00", "time_close":"20:00"}' -H "Content-Type: application/json"  http://127.0.0.1:8000/shop/
    elif request.method == 'POST':
        data = {
           'name': request.data.get('name'),
           'city': request.data.get('city'),
           'street': request.data.get('street'),
           'home': request.data.get('home'),
           'time_open': request.data.get('time_open'),
           'time_close': request.data.get('time_close'),
        }
        serializer = ShopsSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data['id'], status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)