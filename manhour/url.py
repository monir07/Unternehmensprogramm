from django.urls import path, include
from manhour.views import *

urlpatterns = [

    path('manhour',Compose_manhour, name = 'manhour'),
    path('manhour-detail',Manhour_details, name = 'manhour-detail'),
    path('manpower',Compose_attendance, name = 'manpower'),
    path('attend-detail',Attendance_manpower, name = 'attend-detail'),
]