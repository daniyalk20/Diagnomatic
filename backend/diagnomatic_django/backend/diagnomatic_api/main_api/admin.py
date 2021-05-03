from django.contrib import admin
from .models import loggedin_user, pneumonia_data, user
# Register your models here.

admin.site.register(loggedin_user)
admin.site.register(pneumonia_data)
admin.site.register(user)
