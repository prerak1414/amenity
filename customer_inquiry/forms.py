from django import forms
from .models import CustomerInquiry


class CustomerInquiryForm(forms.Form):
	customer_name = forms.CharField(max_length=100)
	email_id = forms.EmailField(max_length=200)
	phone_number = forms.IntegerField()
	customer_complaint_message = forms.CharField()

	expire_date = forms.DateField()