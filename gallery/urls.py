from django.urls import  path
from . import views

app_name = 'gallery'

urlpatterns = [
    path('list/' , views.list , name='list'),

]