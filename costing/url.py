from django.conf.urls import url
from django.urls import path, include
from costing.views import *


urlpatterns = [
    path('costing_section', costing, name='costing_section'),
    path('costing/indent_list', indent_box, name='indent_list'),
    path('mrr_show/costing/<mrr_no>/', mrr_show, name='mrr_show_costing'),
    path('costing/mrr_list', mrr_box, name='mrr_list'),
]