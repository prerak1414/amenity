from django.contrib import admin
from .models import CustomerInquiry

# Register your models here.
class CustomerInquiryAdmin(admin.ModelAdmin):
    list_display = ('customer_name', 'email_id', 'phone_number', 'customer_complaint_message', 'date_added', 'expire_date')
    search_fields = ['customer_name', 'email_id']
    list_per_page = 10


admin.site.register(CustomerInquiry, CustomerInquiryAdmin)