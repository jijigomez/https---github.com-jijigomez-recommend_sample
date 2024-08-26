from django.urls import path
from . import views

urlpatterns = [
    path('tours/', views.tour_list, name='tour_list'),
    path('recommended/', views.recommended_tours, name='recommended_tours'),  # Shows recommended tours
]
