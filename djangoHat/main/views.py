from django.contrib.auth import authenticate, login as user_login, logout as user_logout
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from .models import Products




def index(request):
	products = Products.objects.all()
	return render(request, 'main/index.html', {'products':products})


def regaut(request):
	try:
		if request.method == 'POST':
			login = request.POST.get('login')
			password = request.POST.get('password')

			usr = authenticate(request, username=login, password=password)
			if usr is not None:
				user_login(request, usr)
				return HttpResponseRedirect('/')
			else:
				return render(request, 'main/regaut.html')
	except:
		return render(request, 'main/regaut.html')

	return render(request, 'main/regaut.html')


def register(request):
	try:
		if request.method == 'POST':
			login = request.POST.get('login')
			password = request.POST.get('password')
			password2 = request.POST.get('password2')

			if password == password2:

				User.objects.create_user(login, '', password)

				usr = authenticate(request, username=login, password=password)
				if usr is not None:
					user_login(request, usr)
					return HttpResponseRedirect('/')
				else:
					return render(request, 'main/register.html')
	except:
		return render(request, 'main/register.html')

	return render(request, 'main/register.html')

def logout(request):
	user_logout(request)
	return HttpResponseRedirect('regaut')

