from django.urls import path
from .views import RegisterView, ConsultantProfileUpdateView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('consultant/profile/', ConsultantProfileUpdateView.as_view(), name='consultant_profile'),
]