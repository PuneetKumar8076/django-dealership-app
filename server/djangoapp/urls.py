from django.urls import path
from . import views

urlpatterns = [
    # 🔥 Q17 (Home / Dealers list)
    path('', views.get_dealers, name='home'),

    # 🔥 Q18 (Filter by state)
    path('dealers/<str:state>/', views.get_dealers_by_state, name='dealers_by_state'),

    # 🔥 Q19 (Dealer details + reviews)
    path('dealer/<int:dealer_id>/', views.dealer_details, name='dealer_details'),

    # Extra pages (already working)
    path('about/', views.about),
    path('contact/', views.contact),
]
