from django.urls import path
from . import views
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.get_dealers, name='home'),
    path('dealers/', views.get_dealers_loggedin, name='dealers'),
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),

    path('dealers/<str:state>/', views.get_dealers_by_state, name='dealers_by_state'),

    path('dealer/<int:dealer_id>/', views.dealer_details, name='dealer_details'),

    # 🔥 Q20
    path('dealer/<int:dealer_id>/review/', views.add_review, name='add_review'),

    path('about/', views.about),
    path('contact/', views.contact),
    path('create-user/', views.create_user),

]