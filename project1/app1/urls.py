from django.urls import path
from .views import *

urlpatterns = [
    path("home/", home, name='home_url'),
    path("verify/<str:token>/", verify, name='verify_url'),
]
