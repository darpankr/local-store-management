
from django.forms import ModelForm

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

from .models import *

class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']


class OwnerForm(ModelForm):
	class Meta:
		model = Owner
		fields = '__all__'
		exclude = ['user']

class PhoneForm(ModelForm):
	class Meta:
		model = Smartphone
		fields = '__all__'
		exclude = ['owner']

class ShopForm(ModelForm):
	class Meta:
		model = Shop
		fields = '__all__'
		exclude = ['owner_name']