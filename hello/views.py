from hello.forms import CreateVideoForm
from django.shortcuts import render
from django.http import HttpResponse
import requests
from operator import attrgetter

from .models import  Greeting, Videos

from django.core.files.storage import FileSystemStorage

from keras.models import load_model
from keras.preprocessing import image
import tensorflow as tf
#from tensorflow import Graph, Session

import json

img_height, img_width=224,224
with open('./model/img_classes.json','r') as f:
    labelInfo = f.read()
    
labelInfo = json.loads(labelInfo)


#model_graph = Graph()
#with model_graph.as_default():
#    tf_session = Session()
#    with tf_session.as_default():
model=load_model('./model/classification.h5')


# Create your views here.
def index(request):
    context = {}
    return render(request, '../templates/index.html', context)
    
def upload_video(request):
    fileObj=request.FILES['filePath']
    fs=FileSystemStorage()
    filePathName=fs.save(fileObj.name,fileObj)
    filePathName=fs.url(filePathName)
    testimage='.'+filePathName
    img = image.load_img(testimage, target_size=(img_height, img_width))
    x = image.img_to_array(img)
    x=x/255
    x=x.reshape(1,img_height, img_width,3)
   # with model_graph.as_default():
    #    with tf_session.as_default():
    predi=model.predict(x)

    import numpy as np
    predictedLabel=labelInfo[str(np.argmax(predi[0]))]

    context={'filePathName':filePathName,'predictedLabel':predictedLabel[1]}
    context = {'filePathName': filePathName, 'predictedLabel':predictedLabel[1]}
    return render(request, '../templates/index.html', context)

def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, "db.html", {"greetings": greetings})
