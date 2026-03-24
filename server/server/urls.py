from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    # Home (optional)
    path('', include('djangoapp.urls')),
]
