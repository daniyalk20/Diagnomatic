from django.urls import path
from . import views

urlpatterns = [
    path('user/', views.userList.as_view()),
    path('pneumonia/', views.pneumoniaList.as_view())
]