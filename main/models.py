from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.





class SiteInfo(models.Model):
    title = models.CharField(max_length=225)
    description = RichTextField()
    location = models.CharField(max_length=225 , default=1)
    phone = models.CharField(max_length=225 , default=1)
    logo = models.ImageField(upload_to = 'logo/%y/%m/%d/')
    email = models.EmailField(default='imsinacoder@gamil.com')
    copyright = models.CharField(max_length=225)




class About(models.Model):
    title = models.CharField(max_length=225)
    description = RichTextField()