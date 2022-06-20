from socket import fromshare
from django import forms
from .models import Student

class updateitem(forms.ModelForm):
    class Meta:
        model = Student
        fields='__all__'
