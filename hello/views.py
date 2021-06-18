from hello.forms import CreateVideoForm
from django.shortcuts import render
from django.http import HttpResponse
import requests
from operator import attrgetter

from .models import  Greeting, Videos

# Create your views here.
def index(request):
    context = {}
    return render(request, '../templates/index.html', context)
    
def upload_video(request):
    context = {}
    
    form = CreateVideoForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.save()
        context['upload_message'] = 'Your video is uploaded succesfully'
        
        form = CreateVideoForm()
    context['form'] = form
    
    read_form = sorted(Videos.objects.all(), key=attrgetter('date_published'))
    context['read_form'] = read_form
    
    return render(request, '../templates/upload_videos.html', context)

def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, "db.html", {"greetings": greetings})
