from django.db import models
from datetime import datetime, date, time

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

    @property
    def open(self):
        dic = {}
        now = datetime.now()
        d = date.today()
        open = datetime.strptime(str(d) + ' ' + self.time_open, "%Y-%m-%d %H:%M")
        close = datetime.strptime(str(d) + ' ' + self.time_close, "%Y-%m-%d %H:%M")
        if now > open and now < close:
            dic['open'] = 1
        else:
            dic['open'] = 0
        return dic['open']

    class Meta:
        unique_together = ('name', 'city', 'street')
