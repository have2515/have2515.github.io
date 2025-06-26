from django.urls import path, include
from . import views

urlpatterns = [
	path('', views.index, name='home'),
	path('register', views.register, name='reg'),
	path('login', views.login, name='log'),
	path('logout', views.logout, name='logout')
]