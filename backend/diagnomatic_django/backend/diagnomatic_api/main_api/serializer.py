from rest_framework import serializers
from .models import loggedin_user, pneumonia_data, user

class loggedin_userSerializers(serializers.ModelSerializer):
    class Meta:
        model = loggedin_user
        fields = '__all__'

class userSerializers(serializers.ModelSerializer):
    class Meta:
        model = user
        fields = '__all__'

class pneumonia_dataSerializers(serializers.ModelSerializer):
    class Meta:
        model = pneumonia_data
        fields = '__all__'
