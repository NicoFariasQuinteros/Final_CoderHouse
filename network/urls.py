from django.urls import path
from . import views


app_name = 'network'

urlpatterns = [
    path('', views.home, name='home'),
]