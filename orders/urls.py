from django.urls import path, include
from .views import *


urlpatterns = [
    path('', order_list, name='order_list'),
    path('create/', create_order, name='create_order'),
    path('progress/', order_progress, name='order_progress'),
]
