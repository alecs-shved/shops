from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Q
from .models import City, Street, Shops
from .serializers import CitySerializer, StreetSerializer, ShopsallSerializer
from datetime import datetime, date, time
import json

# Create your views here.

@api_view(['GET', 'POST'])
def get_post_citys(request):
    # get all city. Pos a
    if request.method == 'GET':
        citys = City.objects.filter()
        serializer = CitySerializer(citys, many=True)
        return Response(serializer.data)
    # insert a new record for a city
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
    if request.method == 'GET':
        streets = Street.objects.filter()
        serializer = StreetSerializer(streets, many=True)
        return Response(serializer.data)
    # insert a new record for a street
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
    search_terms = {}
    search_terms['street__name'] = request.GET.get('street')
    search_terms['city__name'] = request.GET.get('city')
    op = request.GET.get("open")
    if op == 1:
        ope = True
    else:
        ope = False
    if request.method == 'GET':
        if op is None: 
            shops = Shops.objects.filter(**search_terms)
        else:
            shops = filter(lambda x: x.open != ope, Shops.objects.filter(**search_terms))
        serializer = ShopsallSerializer(shops, many=True)
        return Response(serializer.data)
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
    
