from django.urls import path
from .views import*


urlpatterns = [
    path('', Task.as_view(), name = 'Home'),
]