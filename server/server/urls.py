from django.contrib import admin
from django.urls import path
from djangoapp import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.get_dealers, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
]
