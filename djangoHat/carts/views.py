from django.shortcuts import render, redirect
from main.models import Products
from carts.models import Cart
# Create your views here.

def cart_add(request, product_slug):
	product = Products.objects.get(name=product_slug)

	carts = Cart.objects.filter(user=request.user, product=product)

	if carts.exists():
		cart = carts.first()
		if cart:
			cart.quantity += 1
			cart.save()
	else:
		Cart.object.create(user.request.user, product=product, quantity=1)

	return redirect(request.META['HTTP_REFERER'])

def cart_change(request, product_slug):
	...


def cart_remove(request, product_slug):
	...


def cart(request):
	return render(request, 'carts/included_cart.html')
