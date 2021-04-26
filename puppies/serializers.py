from rest_framework import serializers
from django.db import models
from .models import City, Street, Shops

class Open():
    open = 0

class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ('name',)

class StreetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Street
        fields = ('name','city',)

class ShopsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shops
        fields = ('id', 'name','city','street','home','time_open','time_close')

class ShopsallSerializer(serializers.ModelSerializer):
    city_name = serializers.ReadOnlyField(source='city.name')
    street_name = serializers.ReadOnlyField(source='street.name')

    class Meta:
        model = Shops
        fields = ('id', 'name', 'city_name', 'street_name','home','time_open','time_close','open')

    def to_representation(self, instance):
        data = super(ShopsallSerializer, self).to_representation(instance)
        if data.get('open') == Open.open:
            return None
        return data
