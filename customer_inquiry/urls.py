from django.urls import path, include
from .views import create_inquiry, otp

urlpatterns = [
	path('' , create_inquiry , name="create_inquiry"),
	path('otp/' , otp , name="otp_page"),
]