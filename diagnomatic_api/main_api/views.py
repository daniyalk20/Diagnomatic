from django.shortcuts import render
from rest_framework.views import APIView
from .serializer import loggedin_userSerializers, pneumonia_dataSerializers, userSerializers
from .models import user, loggedin_user, pneumonia_data
from rest_framework.response import Response


# Create your views here.
class userList(APIView):
    def get(self, request):
        userList = user.objects.all()
        serialize = userSerializers(userList, many=True)
        return Response(serialize.data)

class pneumoniaList(APIView):
    def get(self, request):
        pneumoniaList = pneumonia_data.objects.all()
        serialize = pneumonia_dataSerializers(pneumoniaList, many=True)
        return Response(serialize.data)
