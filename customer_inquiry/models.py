from django.db import models

# Create your models here.

class CustomerInquiry(models.Model):
	customer_name = models.CharField(max_length=100)
	email_id = models.EmailField(max_length=200)
	phone_number = models.IntegerField(null=False, blank=False)
	customer_complaint_message = models.TextField(blank = True)
	otp = models.CharField(max_length=6)
	date_added = models.DateField(auto_now_add=True)
	expire_date = models.DateField(null=True, blank=True)