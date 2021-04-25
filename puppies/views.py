#from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Q
from .models import City, Street, Shops
from .serializers import CitySerializer, StreetSerializer, ShopsSerializer, ShopsallSerializer
from datetime import datetime, date, time
import json

# Create your views here.

@api_view(['GET', 'POST'])
def get_post_citys(request):
    # get all city. Pos a
    #curl  -v -X GET -H "Content-Type: application/json"  http://127.0.0.1:8000/city/
    if request.method == 'GET':
        citys = City.objects.filter()
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
        streets = Street.objects.filter()
        serializer = StreetSerializer(streets, many=True)
        return Response(serializer.data)
    # insert a new record for a street
    #curl  -v -X POST --data '{"name":"Malina-street","city":1}' -H "Content-Type: application/json"  http://127.0.0.1:8000/city/street/
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
    # curl  -v -X GET -H "Content-Type: application/json"  http://127.0.0.1:8000/shop/?q=shop-six%Kupustin-Yar%Malina-street%0
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
        if i == 4:
            open = int(search_terms['open'])
            del search_terms['open'] 
        shops = Shops.objects.all().filter(**search_terms)
        serializer = ShopsallSerializer(shops, many=True)
        if i == 4:
            serial_data = []
            for j in serializer.data:
                if j['open'] != open:
                    serial_data.append(j)
            return Response(serial_data)  
        return Response(serializer.data)
    #?q=shop-six%Kupustin-Yar%Malina-street%0
    #curl  -v -X POST --data '{"name":"shop-six","city":1,"street":1,"home":14,"time_open":"08:00","time_close":"20:00"}' -H "Content-Type: application/json"  http://127.0.0.1:8000/shop/
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
    
