from django import forms
from .models import Contact


class PostForm(forms.ModelForm):



    class Meta:
        model = Contact
        fields = ('name' , 'email' , 'phone' , 'message')

    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        self.fields['name'].label = "نام"
        self.fields['email'].label = "ایمیل"
        self.fields['phone'].label = "شماره تلفن"
        self.fields['message'].label = "پیغام"
