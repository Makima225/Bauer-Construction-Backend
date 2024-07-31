from django.urls import path
from core.views import ListHouseView, DetailHouseView, CreateContactView

urlpatterns = [
    path('house/', ListHouseView.as_view()),
    path('house-detail/<int:pk>/', DetailHouseView.as_view()),
    path('contact-us/', CreateContactView.as_view()),
]