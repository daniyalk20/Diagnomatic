from django.db import models

# Create your models here.
from django.utils import timezone


class user(models.Model):
    user_lname = models.CharField(null=False, max_length=100)
    user_fname = models.CharField(null=False, max_length=100)
    username = models.CharField(null=False, max_length=50, unique=True, default='null')
    password = models.CharField(null = False, max_length=256)
    email_id = models.EmailField(null=False)
    lastloggedin = models.DateTimeField(null=False, default=timezone.now)

    def __str__(self):
        return "%s %s" % (self.user_fname, self.user_lname)

class loggedin_user(models.Model):
    token = models.CharField(null=False, max_length=256, unique=True)
    loginTime = models.DateTimeField(null=False, default=timezone.now)

class pneumonia_data(models.Model):
    img_id = models.ForeignKey(user, on_delete=models.CASCADE, primary_key=True)
    name = models.CharField(null=False, max_length=50)
    image = models.ImageField(upload_to='pneumonia')