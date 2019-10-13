import os
import requests
from django.shortcuts import render
from django.http import HttpResponse
from .models import locationdata, authoritydata, userdata
from django.core.files.storage import FileSystemStorage
import numpy as np
import matplotlib.pyplot as plt
import cv2
import keras
from keras.models import Sequential, load_model

api_key = 'MRYGgqUTWvlAdwmSxAZyF19gfic1KWzx'
wrongpass = 'Invalid Username or Password'

def index(request):
    return render(request, 'index.html')

def signup(request):
    return render(request, 'index.html')

def usemodel(path):

    model = load_model.weights('../home/best_waste_classifier.h5')
    pic = plt.imread(path)
    pic = cv2.resize(pic, (b,h))
    pic = np.expand_dims(pic, axis=0)
    classes = model.predict_classes(pic)

    return classes

def login(request):
    username = request.POST['modalLRInput10']
    password = request.POST['modalLRInput11']
    users = userdata.objects.all()
    locations = locationdata.objects.all()
    try:
        user = users.get(username = username)
        print("Record Found")
    except Exception as e:
        return render(request, 'index.html', {'wrongpass':wrongpass})

    if(password == user.password):
        location = user.locationdata_set.all()
        # location = locations.get(contributor = user)
        return render(request,'map.html',{'user':user , 'location': location })
    else:
        return render(request, 'index.html', {'wrongpass':wrongpass})

def app(request):
        users = userdata.objects.all()
        user = users.get(pk=1)
        locations = locationdata.objects.all()
        address = request.POST['inputAddress']
        image = request.FILES['myFile']
        print(image.name, image.size)
        fs = FileSystemStorage()
        filename = fs.save(image.name, image)
        # print(usemodel('../media/'+ str(image.name)))
        urlmap = 'https://www.mapquestapi.com/staticmap/v5/map?key=MRYGgqUTWvlAdwmSxAZyF19gfic1KWzx&locations='
        loc = urlmap + address
        result = requests.get(loc).json()
        print(result)
        lat = result.results[0].locations[0].latLng.lat
        lon = result.results[0].locations[0].latLng.lon
        print(lat,lon)
        # user.locationdata_set.create(location = address, pic = image, lat= lat, lon=lon)

        return render(request,'map.html',{'user':user, 'loc':loc})