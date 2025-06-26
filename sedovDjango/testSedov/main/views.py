from django.shortcuts import render
from django.contrib.auth import authenticate, login as user_login, logout as user_logout
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from .models import Products
# Create your views here.

def index(request):
	products = Products.objects.all()
	return render(request, 'index.html', {'products':products})


def register(request):
	if request.method == 'POST':
		name = request.POST.get('name')
		password = request.POST.get('password')

		usr = authenticate(request, username=name, password=password)

		User.objects.create_user(name, '', password)

		if usr is not None:
			user_login(request, usr)
			return HttpResponseRedirect('/')
		else:
			return render(request, 'registration.html')

	return render(request, 'registration.html')

def login(request):
	if request.method == 'POST':
		name = request.POST.get('name')
		password = request.POST.get('password')

		usr = authenticate(request, username=name, password=password)
		if usr is not None:
			user_login(request, usr)
			return HttpResponseRedirect('/')
		else:
			return render(request, 'login.html')

	return render(request, 'login.html')

def logout(request):
	user_logout(request)
	return HttpResponseRedirect('/')
