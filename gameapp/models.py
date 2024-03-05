from django.db import models
from django.utils.timezone import now

# Create your models here.
class Game(models.Model):
    name = models.CharField(max_length=150, default="")
    code = models.CharField(max_length=150, default="")
    studio = models.CharField(max_length=150, default="")
    release_date = models.DateField(default=now)
    thumbnail = models.CharField(max_length = 250, default="")
    img1 = models.CharField(max_length = 250, default="")
    img2 = models.CharField(max_length = 250, default="")
    img3 = models.CharField(max_length = 250, default="")
    img4 = models.CharField(max_length = 250, default="")
    price = models.IntegerField(default=0)
    
class Users(models.Model):
    username = models.CharField(max_length = 150)
    password = models.CharField(max_length=200)