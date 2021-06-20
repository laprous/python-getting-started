from django.urls import path, include

from django.contrib import admin

admin.autodiscover()

from django.conf.urls import url

from django.conf.urls.static import static
from django.conf import settings

import hello.views

# To add a new path, first import the app:
# import blog
#
# Then add the new path:
# path('blog/', blog.urls, name="blog")
#
# Learn more here: https://docs.djangoproject.com/en/2.1/topics/http/urls/

urlpatterns = [
    path("", hello.views.index, name="index"),
    path("admin/", admin.site.urls),
   # path('upload-video/', hello.views.upload_video, name='upload-video'),
    url('predictVideo/', hello.views.upload_video, name='predictVideo')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
