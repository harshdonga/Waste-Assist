from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class userdata(models.Model):
    name = models.CharField(max_length = 500)
    username = models.CharField(max_length = 500)
    password = models.CharField(max_length = 500)
    city = models.CharField(max_length = 500)
    phone = models.IntegerField(validators = [ MinValueValidator(1000000000) , MaxValueValidator(9999999999)])
    mycredits = models.IntegerField(default = 0)
    mypoints = models.IntegerField(default = 0)

    def __str__(self):
        return self.username + '-'+ self.city

class locationdata(models.Model):
    contributor = models.ForeignKey(userdata, on_delete=models.CASCADE)
    location = models.CharField(max_length = 500)
    pic = models.ImageField(upload_to = 'images', blank = True)
    lat = models.IntegerField()
    lon = models.IntegerField()

    def __str__(self):
        return self.location + '-' +str(self.contributor)

class authoritydata(models.Model):
    area = models.CharField(max_length = 500)
    users = models.IntegerField()
