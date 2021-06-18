from django.db import models

def upload_location_video(instance, filename, **kwargs):
    file_path = 'hello/{video_name}/{date_published}-{filename}'.format(
        title=str(instance.video_name), filename=filename
    )

class Videos(models.Model):
    video = models.FileField(upload_to=upload_location_video, null=False, blank=False)
    date_published = models.DateTimeField(auto_now_add=True, verbose_name='date published published')
    video_name = models.CharField(max_length=200, null=False, blank=False)
    
    def __str__(self):
        return self.video_name

# Create your models here.
class Greeting(models.Model):
    when = models.DateTimeField("date created", auto_now_add=True)
