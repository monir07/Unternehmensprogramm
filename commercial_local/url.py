from django.conf.urls import url
from django.urls import path, include
from commercial_local.views import *


urlpatterns = [
    path('commercial_l', commercial_local, name='commercial_l'),
]