from django.db import models

# Create your models here.

class City(models.Model):
    name = models.CharField(max_length=30, unique=True)

    def __str__(self):
       return self.name
    
    def get_breed(self):
        return self.name + ' belongs to '

    def __repr__(self):
        return self.name + ' is added.'

class Street(models.Model):
    name = models.CharField(max_length=30)
    city = models.ForeignKey(City, on_delete = models.CASCADE)

    def __str__(self):
       return self.name

    def get_breed(self):
        return self.name + ' belongs to '

    def __repr__(self):
        return self.name + ' is added.'

class Shops(models.Model):
    name = models.CharField(max_length=30, unique=True)
    city = models.ForeignKey(City, on_delete = models.CASCADE)
    street = models.ForeignKey(Street, on_delete = models.CASCADE)
    home = models.IntegerField(default=1)
    time_open = models.CharField(max_length=15)
    time_close = models.CharField(max_length=15)
    
    #@property
    #def city_name(self):
    #    cit = self.street.city_id
    #    return cit.city_id

    #@property
    #def street_name(self):
     #   return self.street.name

    @property
    def open(self):
        return 0

    class Meta:
        unique_together = ('name', 'city', 'street')
