from django.urls import  path
from . import views

app_name = 'services'

urlpatterns = [
    path('list/' , views.list , name='list'),
]