from django.shortcuts import render
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
    try:
        city = City.objects.get(pk=pk)
    except City.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    # get details of a single puppy
    if request.method == 'GET':
        return Response({'get':'well'})
    # delete a single puppy
    elif request.method == 'DELETE':
        return Response({'del':'well'})
    # update details of a single puppy
    elif request.method == 'PUT':
        return Response({'put':'well'})


@api_view(['GET', 'POST'])
def get_post_citys(request):
    # get all city
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
    # get all street
    if request.method == 'GET':
        streets = Street.objects.filter()
        serializer = StreetSerializer(streets, many=True)
        return Response(serializer.data)
    # insert a new record for a city
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
    # get all street
    if request.method == 'GET':
        shopss = Shops.objects.filter()
        lis = []
        for sh in shopss:
            dic = {}
            dic['name'] = sh.name
            #(Street.objects.get(id=sh.street_id)).city_id)
            dic['city'] = str((City.objects.get(id=sh.street_id)).name)
            dic['street'] = str((Street.objects.get(id=sh.street_id)).name)
            dic['home'] = sh.home
            dic['date_open'] = sh.date_open
            dic['date_close'] = sh.date_close
            lis.append(dic)    
        print(lis)
        serializer = ShopsSerializer(lis, many=True)
        return Response(serializer.data)
    # insert a new record for a city
    elif request.method == 'POST':
        streets = Street.objects.all()
        for shops in SHOPS:
            shop = Shops()
            shop.name = shops
            shop.street_id = streets[random.randrange(len(streets))].city_id
            shop.city = shop.street_id
            shop.home = random.randrange(29)
            shop.date_open = '8:00'
            shop.date_close = '20:00'
            shop.save()
        return Response({'insert': 'shop good'})