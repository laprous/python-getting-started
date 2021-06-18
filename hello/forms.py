from hello.models import Videos
from django import forms



class CreateVideoForm(forms.ModelForm):
    class Meta:
        model = Videos
        fields = ['video_name', 'video']