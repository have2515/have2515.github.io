from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
	path('', views.index, name='home'),
	path('regaut', views.regaut, name='regaut'),
	path('register', views.register, name='register'),
	path('logout', views.logout)

]

