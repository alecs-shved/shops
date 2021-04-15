from django.db import models

# Create your models here.
class City(models.Model):
    name = models.CharField(max_length=30)
    
    def get_breed(self):
        return self.name + ' belongs to '

    def __repr__(self):
        return self.name + ' is added.'

class Street(models.Model):
    name = models.CharField(max_length=30)
    city = models.ForeignKey(City, on_delete = models.CASCADE)

class Shops(models.Model):
    name = models.CharField(max_length=30)
    city = models.ForeignKey(City, on_delete = models.CASCADE)
    street = models.ForeignKey(Street, on_delete = models.CASCADE)
    home = models.IntegerField(default=1)
    date_open = models.DateTimeField(default='8:00')
    date_close = models.DateTimeField(default='20:00')
