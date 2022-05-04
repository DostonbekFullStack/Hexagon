from dataclasses import field, fields
from pyexpat import model
from .models import SignUp
from django.forms import ModelForm

class SignUpForm(ModelForm):
    class Meta:
        model = SignUp
        fields = '__all__'