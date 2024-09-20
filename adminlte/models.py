from django.db import models
import datetime
import os

from django.db.models.deletion import SET_NULL


# Create your models here.

def filepath(instace, filename):
    old_fileName = filename
    currentTime = datetime.datetime.now().strftime('%Y%m%d%H:%M:%S')
    filename = "%s%s" % (currentTime, old_fileName)
    return os.path.join('products/', filename)

class Category(models.Model):
    name = models.CharField(max_length=255, null=False)
    
    def __str__(self) -> str:
        return self.name



class Product(models.Model):
    availability = ((0, 'Out Of Stock'),(1, 'Active'))
    name = models.CharField(max_length=255, null=False)
    desc = models.CharField(max_length=1000, null=True)
    price = models.DecimalField(default=0, max_digits=6, decimal_places=1) # 9999.99
    status = models.IntegerField(choices=availability, default=0)
    image = models.ImageField(upload_to=filepath, blank=True,  null=True)
    category = models.ForeignKey('Category', on_delete=SET_NULL, null=True)

    
    def __str__(self) -> str:
        return self.name


