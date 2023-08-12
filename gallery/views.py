from django.shortcuts import render , redirect , HttpResponse
from main.models import SiteInfo , About
from .models import Gallery

# Create your views here.



def list(request):
    information = SiteInfo.objects.last()
    about = About.objects.last()
    galleries = Gallery.objects.all()
    title = "گالری"
    context = {
        'title' : title,
        "information" : information,
        "about" : about,
        "galleries" : galleries,
    }
    return render(request , 'gallery/list.html' , context)

