from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Q
from .models import City, Street, Shops
from .serializers import CitySerializer, StreetSerializer, ShopsSerializer, ShopsallSerializer, Open
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
    query = request.GET.get("q")
    if request.method == 'GET':
        if query is None: 
            shops = Shops.objects.all()  
            serializer = ShopsallSerializer(shops, many=True)
            return Response(serializer.data)
        search_terms = {}
        query_plan = ['name','city__name','street__name', 'open']
        i = 0
        for v in query.split("%"):
            search_terms[query_plan[i]] = v
            i = i + 1
        try:
            Open.open = int(search_terms['open'])
            del search_terms['open'] 
        except:
            shops = Shops.objects.all().filter(**search_terms)
            serializer = ShopsallSerializer(shops, many=True)
            return Response(serializer.data)
        shops = Shops.objects.all().filter(**search_terms)
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
    
