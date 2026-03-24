from django.urls import path
from . import views

urlpatterns = [
    path('dealers', views.get_dealers_loggedin, name='dealers'),
]
