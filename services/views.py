from django.shortcuts import render , redirect , HttpResponse
from main.models import SiteInfo , About

from .models import Services
# Create your views here.

def list(request):
    information = SiteInfo.objects.last()
    about = About.objects.last()
    services = Services.objects.all()
    title = "سرویس ها"
    context = {
        'title' : title,
        "information" : information,
        "about" : about,
        "services" : services,
    }
    return render(request , 'service/list.html' , context)
