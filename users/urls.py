from django.urls import path
from .views import RegisterView, ConsultantProfileUpdateView
from .views import VerifyConsultantView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('consultant/profile/', ConsultantProfileUpdateView.as_view(), name='consultant_profile'),
    path("verify-consultant/<int:pk>/", VerifyConsultantView.as_view()),
]