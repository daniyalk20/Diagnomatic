from django.db import models
from django import forms
from django.db.models.base import Model

# Create your models here.

class user_info(models.Model):
    uid = models.AutoField(primary_key=True)
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)

class user_data(models.Model):
    uid = models.ForeignKey(user_info, on_delete=models.CASCADE)
    name = models.CharField(max_length=2000)
    email = models.EmailField()