from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib import sessions
from django.contrib.auth.decorators import login_required
import requests


# URLs
Mech_url = "http://127.0.0.1:8000/api/mechs/"
Car_url = "http://127.0.0.1:8000/api/cars/"
User_url = "http://127.0.0.1:8000/api/users/"
Cbook_url = "http://127.0.0.1:8000/api/cbookings/"
Mbook_url = "http://127.0.0.1:8000/api/mbookings/"
# res = requests.get(Mech_url).json()
resc = requests.get(Car_url).json()

# ---------------------------------------------------------------------FORM-------------------------------------------------------------------------------

@login_required
def car_form_view(request):
	try:
		context = {}
		if request.method == "POST":
			cemailid = request.POST['Email_id']
			costperday = request.POST['cost']
		context['car_id'] = cemailid		
		context['email_id'] = request.user.email
		context['amount'] = costperday
		return render(request, 'carform.html', context)
	except:
		return redirect('car')

@login_required
def mech_form_view(request):
	try:
		context = dict()
		if request.method == "POST":
			memailid = request.POST['Email_id']
			charge = request.POST['cost']
		context['mech_id'] = memailid
		context['email_id'] = request.user.email
		context['amount'] = charge
		return render(request, 'mechform.html', context)
	except:
		return redirect('mechanic')

# ---------------------------------------------------------------------PAYMENT---------------------------------------------------------------------------
@login_required
def car_payment_view(request):
	try: 
		context = {}
		if request.method == "POST":
			context['fname'] = request.POST['fname']
			context['lname'] = request.POST['lname']
			context['uname'] = request.POST['username']
			context['gender'] = request.POST['gender']
			context['age'] = request.POST['age']
			context['email_id'] = request.POST['email_id']
			context['car_id'] = request.POST['car_id']
			context['contact'] = request.POST['contact']
			context['licenseno'] = request.POST['dLicense']
			context['price'] = int(request.POST['amount'])*int(request.POST['days'])
		
		if requests.get(User_url+context['email_id']).json() == []:
			ur = {"email_id": context['email_id'],
				"fname": context['fname'],
				"lname": context['lname'],
				"username": context['uname'],
				"age": context['age'],
				"gender": context['gender'],
				"contact": context['contact'],
				"dLicense": context['licenseno']
				}
			usrres1 = requests.post(User_url,json=ur)

		curl =	Car_url+ context['car_id']
		counterc = requests.get(Cbook_url).json()
		cc = counterc[len(counterc)-1]['sr'] + 10
		r = requests.get(curl).json()[0]
		if r['is_available'] == False:
			return redirect('car')
		else:
			r['is_available'] = False
			r['earnings'] += context['price']
			x = {"sr": cc,
				"buyer_email": context['email_id'],
				"car_name": r['car_name'],
				"car_number": r['car_number'],
				"owner_email": context['car_id'],
				"status": "Aproved"}
			resp1 = requests.post(Cbook_url, json=x)
			resp2 = requests.post(Car_url, json=r)
		resc = requests.get(Car_url).json()
		return render(request, 'carpayment.html', context)
	except:
		return redirect('car')

@login_required
def mech_payment_view(request):
	try:
		context = {}
		if request.method == "POST":
			context['fname'] = request.POST['fname']
			context['lname'] = request.POST['lname']
			context['uname'] = request.POST['username']
			context['gender'] = request.POST['gender']
			context['email_id'] = request.POST['email_id']
			context['mech_id'] = request.POST['mech_id']
			context['contact'] = request.POST['contact']
			context['price'] = int(request.POST['amount'])
		ur = User_url + context['email_id']
		if requests.get(ur).json() == []:
			ur = {"email_id": context['email_id'],
				"fname": context['fname'],
				"lname": context['lname'],
				"username": context['uname'],
				"age": 20,"gender": 'NA',
				"contact": context['contact'],
				"dLicense": 'NA'}
			usrres1 = requests.post(User_url,json=ur)

		counterm = requests.get(Mbook_url).json()
		cm = counterm[len(counterm)-1]['sr'] + 1
		curl =	Mech_url+ context['mech_id']
		r = requests.get(curl).json()[0]
		if r['is_available'] == False:
			return redirect('mechanic')
		else:
			r['earnings'] += context['price']
			x = {"sr": cm,
				"buyer_email": context['email_id'],
				"mech_email": context['mech_id'],
				"status": "Aproved"}
			resp1 = requests.post(Mbook_url, json=x)
			resp2 = requests.post(Mech_url, json=r)
		return render(request, 'mechpayment.html', context)
	except:
		return redirect('mechanic')

# -----------------------------------------------------------------------PAGES-------------------------------------------------------------------------
def images():
	L = ["https://imgd.aeplcdn.com/1056x594/n/cw/ec/20623/innova-crysta-exterior-right-front-three-quarter.jpeg?q=85","https://imgd.aeplcdn.com/1056x594/cw/ec/20442/Mercedes-Benz-GLE-Class-Right-Front-Three-Quarter-58803.jpg?v=201711021421&q=85",
			"https://imgd.aeplcdn.com/1056x594/cw/ec/19826/Jaguar-XF-Right-Front-Three-Quarter-80407.jpg?v=201711021421&q=85","https://imgd.aeplcdn.com/1056x594/n/cw/ec/44879/landrover-discovery-sport-front-view15.jpeg?q=85",
			"https://imgd.aeplcdn.com/1056x594/n/cw/ec/49098/mustang-facelift-exterior-left-rear-three-quarter.jpeg?q=85","https://imgd.aeplcdn.com/1056x594/n/cw/ec/25107/compass-exterior-left-front-three-quarter-3.jpeg?q=85",
			"https://imgd.aeplcdn.com/1056x594/n/cw/ec/34024/xuv500-exterior-left-front-three-quarter.jpeg?q=85","https://imgd.aeplcdn.com/1056x594/n/cw/ec/45691/marutisuzuki-dzire-right-front-three-quarter8.jpeg?q=85",
			"https://imgd.aeplcdn.com/1056x594/cw/ec/26588/Toyota-Corolla-Altis-Exterior-92968.jpg?v=201711021421&q=85","https://imgd.aeplcdn.com/1056x594/n/cw/ec/40535/all-new-city-exterior-right-front-three-quarter.jpeg?q=85",
			"https://imgd.aeplcdn.com/1056x594/n/cw/ec/41523/sonet-exterior-right-front-three-quarter-108.jpeg?q=85","https://imgd.aeplcdn.com/1056x594/n/cw/ec/27074/civic-exterior-right-front-three-quarter-148155.jpeg?q=85",
			"https://imgd.aeplcdn.com/1056x594/n/cw/ec/51529/x5-m-exterior-right-front-three-quarter.jpeg?q=85","https://imgd.aeplcdn.com/1056x594/n/cw/ec/50151/yaris-black-limited-edition-exterior-left-front-three-quarter-2.jpeg?q=85",
			"https://imgd.aeplcdn.com/1056x594/n/cw/ec/50924/amg-glc-43-coupe-exterior-right-front-three-quarter.jpeg?q=85","https://imgd.aeplcdn.com/1056x594/n/cw/ec/43485/gloster-exterior-right-front-three-quarter-2.jpeg?q=85",
			"https://imgd.aeplcdn.com/1056x594/n/cw/ec/47562/skoda-rapid-tsi-right-front-three-quarter0.jpeg?q=85","https://imgd.aeplcdn.com/1056x594/n/cw/ec/40530/i20-exterior-right-front-three-quarter-5.jpeg?q=85",
			"https://imgd.aeplcdn.com/1056x594/n/cw/ec/39039/superb-exterior-right-front-three-quarter-2.jpeg?q=85","https://imgd.aeplcdn.com/1056x594/n/cw/ec/28783/skoda-octavia-right-front-three-quarter63.jpeg?q=85",
			"https://imgd.aeplcdn.com/1056x594/n/cw/ec/49098/mustang-facelift-exterior-left-front-three-quarter.jpeg?q=85","https://imgd.aeplcdn.com/1056x594/n/cw/ec/37640/endeavour-exterior-right-front-three-quarter-149472.jpeg?q=85",
			"https://imgd.aeplcdn.com/1056x594/n/cw/ec/41217/toyota-vellfire-right-front-three-quarter5.jpeg?q=85","https://imgd.aeplcdn.com/1056x594/n/cw/ec/44709/toyota-fortuner-facelift-right-front-three-quarter2.jpeg?q=85",
			"https://imgd.aeplcdn.com/1056x594/n/cw/ec/19812/fortuner-exterior-right-front-three-quarter-2.jpeg?q=85"]

	return L

@login_required
def home_view(request):
	context = dict()
	return render(request, 'home.html', context)

@login_required
def car_view(request):
	try:
		L = images()
		context = dict()
		resc = requests.get(Car_url).json()
		j = 0
		for i in resc:
			i['img'] = L[j%len(L)]
			j+=1
		context['carlist'] = resc
		return render(request,'car.html', context)
	except:
		return redirect('dashboard')

@login_required
def mechanic_view(request):
	try:
		context = dict()
		context['mechaniclist'] = res
		return render(request,'mechanic.html', context)
	except:
		return redirect('dashboard')

@login_required
def contact_view(request):
	context = dict()
	context['contact'] = [{'heading':'Accounts section', 'email': 'accounts@modelapp.com', 'contact': '9918201173'},
						  {'heading':'Admin section', 'email': 'admin@modelapp.com', 'contact': '9918201174'},
						  {'heading':'Booking Related', 'email': 'bookings@modelapp.com', 'contact': '9918201175'}]
	return render(request, 'contact.html', context)

@login_required
def dashboard_view(request):
	context = dict()
	context['udata'] = {'name': request.user.first_name + " " + request.user.last_name, 
						'email_id': request.user.email, 'username': request.user.username}
	urlc = Cbook_url + request.user.email
	urlm = Mbook_url + request.user.email
	context['car'] = requests.get(urlc).json()
	context['mech'] = requests.get(urlm).json()
	return render(request,'dashboard.html', context)

# ---------------------------------------------------------------------------------------------------------------------------------------------------#
