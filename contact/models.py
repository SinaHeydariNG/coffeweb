from django.db import models

# Create your models here.



class Contact(models.Model):
    name = models.CharField(max_length=225)
    email = models.EmailField()
    phone = models.CharField(max_length=225)
    message = models.TextField()
    activate = models.BooleanField(default=False , null=True , blank=True)