from django.shortcuts import render , redirect , HttpResponse
from .models import SiteInfo , About
from gallery.models import Gallery
from services.models import Services
from contact.forms import PostForm
from contact.models import Contact
# Create your views here.

def home(request):
    information = SiteInfo.objects.last()
    about = About.objects.last()
    galleries = Gallery.objects.all()
    services = Services.objects.all()
    add_message = PostForm()
    feedbacks = Contact.objects.filter(activate = True)
    title = "خانه"
    context = {
        'title' : title,
        "information" : information,
        "about" : about,
        "galleries" : galleries,
        "services" : services,
        "add_message" : add_message,
        "feedbacks" : feedbacks
    }
    return render(request , 'main/home.html' , context)


def about(request):
    information = SiteInfo.objects.last()
    about = About.objects.last()
    title = "درباره ما"
    context = {
        'title' : title,
        "information" : information,
        "about" : about,
    }
    return render(request , 'main/about.html' , context)

