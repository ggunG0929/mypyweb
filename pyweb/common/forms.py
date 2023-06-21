from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserForm(UserCreationForm):   # import
    last_name = forms.CharField(max_length=20)  # import django.forms
    email = forms.EmailField()

    class Meta:
        model = User    # import
        fields = ['username', 'last_name', 'email']
