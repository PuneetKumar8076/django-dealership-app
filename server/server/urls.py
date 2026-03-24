from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    # Home (optional)
    path('', include('djangoapp.urls')),
]
from django.contrib import admin
from django.urls import path
from djangoapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.get_dealers),
    path('dealers/', views.get_dealers),
    path('about/', views.about),
    path('contact/', views.contact),
]
