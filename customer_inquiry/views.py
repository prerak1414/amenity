import random
from django.shortcuts import render, redirect
from .models import CustomerInquiry
import http.client
from django.conf import settings

def send_otp(phone, otp):
	conn = http.client.HTTPSConnection("2factor.in")
	headers = {'content-type': "application/x-www-form-urlencoded"}
	authkey = settings.AUTH_KEY 
	payload = ""
	url = f"https://2factor.in/API/V1/{authkey}/SMS/{phone}/{otp}"
	conn.request("GET", url , payload, headers)
	res = conn.getresponse()
	data = res.read()
	print(data.decode("utf-8"))
	return None

def otp(request):
	phone = request.session['phone']
	print(phone)
	if request.method == "POST":
		otp = request.POST.get('otp')
		print(otp)
		inquiry = CustomerInquiry.objects.filter(phone_number=phone).last()
		print(inquiry.id)
		if otp == inquiry.otp:
			context = {'message' : 'OTP VERIFIED'}
		else:		
			context = {'message' : 'Please provide valid OTP'}
		return render(request, 'otp.html', context)
		
	return render(request, 'otp.html')

def create_inquiry(request):
	if request.method == "POST":
		customer_name = request.POST.get('name')
		email = request.POST.get('email')
		phone = request.POST.get('phone')
		complaint = request.POST.get('complaint')
		end_date = request.POST.get('end_date')

		otp = str(random.randint(100000, 999999))
		
		# email regex
		email_regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

		if not customer_name and not phone and not email:
			context = {'message' : 'Pease enter Customer Details'}
			return render(request, 'inquiry.html' , context)
		elif not (re.fullmatch(email_regex, email)): 
			context = {'message' : 'Pease enter valid email address'}
			return render(request, 'inquiry.html' , context)
		elif len(phone) != 10:
			context = {'message' : 'Pease enter valid phone number'}
			return render(request, 'inquiry.html' , context)
		elif phone and customer_name and email:
			details = CustomerInquiry(customer_name=customer_name, email_id=email, phone_number=phone, customer_complaint_message=complaint, otp=otp, expire_date=end_date)
			details.save()
			send_otp(phone, otp)
			request.session['phone'] = phone

			return redirect('otp_page')
		else:
			context = {'message' : 'Proper Customer Details not entered'}
			return render(request, 'inquiry.html' , context)

	return render(request, 'inquiry.html')
