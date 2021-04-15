from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import City, CITYS
from .serializers import CitySerializer

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
        puppies = City.objects.all()
        serializer = CitySerializer(puppies, many=True)
        return Response(serializer.data)
    # insert a new record for a city
    elif request.method == 'POST':
        for cit in CITYS:
            city = City()
            city.name = cit
            city.save()
        return Response({'insert':'good'})
