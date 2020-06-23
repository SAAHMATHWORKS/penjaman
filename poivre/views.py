from django.shortcuts import render, get_object_or_404 
from django.http import JsonResponse, HttpResponse
from django.core.mail import send_mail, BadHeaderError
from django.conf import settings
from .models import * 
import json
import datetime
from .utils import cookieCart, cartData, guestOrder
from django.contrib.auth.models import User
# Create your views here.

def home(request):
	data = cartData(request)

	cartItems = data['cartItems']

	products = Product.objects.all()
	context = {'products':products, 'cartItems':cartItems}
	return render(request, 'poivre/home.html', context)


def contact(request):
    if request.method == 'POST':
        message_name = request.POST['message-name']
        message_email = request.POST['message-email']
        message_subject = request.POST['message-subject'] 
        message_content = request.POST['message'] + 'from this emal: ' + message_email
        print(message_name)
        # send email
        try:
            send_mail(
                message_subject, # subject of message
                f'Message de: {message_name} \n son email est: {message_email} \n Le contenu de son message est: \n  {message_content}', # contenu du message
                settings.EMAIL_HOST_USER, # from email
                ['saahthibaut@gmail.com'], # to email
                fail_silently=False,
            )
            print(message_email)
            msg = "success"
        except BadHeaderError:
            msg = "error"
        return render(request, 'poivre/contact.html', {'msg': msg})
    
    return render(request, 'poivre/contact.html', {})



def store(request):
	data = cartData(request)

	cartItems = data['cartItems']
	order = data['order']
	items = data['items']

	products = Product.objects.all()
	context = {'products':products, 'cartItems':cartItems}
	return render(request, 'poivre/shop.html', context)

def details(request, id):
	data = cartData(request)
	cartItems = data['cartItems']
	product = get_object_or_404(Product, id=id)
	context = {'product':product, 'cartItems':cartItems}
	return render(request, 'poivre/product-single.html', context)


def cart(request):
	data = cartData(request)

	cartItems = data['cartItems']
	order = data['order']
	items = data['items']

	context = {'items':items, 'order':order, 'cartItems':cartItems}
	return render(request, 'poivre/cart.html', context)

def checkout(request):
	data = cartData(request)
	
	cartItems = data['cartItems']
	order = data['order']
	items = data['items']

	context = {'items':items, 'order':order, 'cartItems':cartItems}
	return render(request, 'poivre/checkout.html', context)

def updateItem(request):
	data = json.loads(request.body)
	productId = data['productId']
	action = data['action']
	print('Action:', action)
	print('Product:', productId)

	customer = request.user.customer
	product = Product.objects.get(id=productId)
	order, created = Order.objects.get_or_create(customer=customer, complete=False)

	orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

	if action == 'add':
		orderItem.quantity = (orderItem.quantity + 1)
	elif action == 'remove':
		orderItem.quantity = (orderItem.quantity - 1)

	orderItem.save()

	if orderItem.quantity <= 0:
		orderItem.delete()

	return JsonResponse('Item was added', safe=False)


def processOrder(request):
	transaction_id = datetime.datetime.now().timestamp()
	data = json.loads(request.body)

	if request.user.is_authenticated:
		customer = request.user.customer
		order, created = Order.objects.get_or_create(customer=customer, complete=False)
	else:
		customer, order = guestOrder(request, data)

	total = float(data['form']['total'])
	order.transaction_id = transaction_id

	if total == order.get_cart_total:
		order.complete = True
	order.save()

	if order.shipping == True:
		ShippingAddress.objects.create(
		customer=customer,
		order=order,
		address=data['shipping']['address'],
		city=data['shipping']['city'],
		state=data['shipping']['state'],
		phone=data['shipping']['phone'],
		)

	return JsonResponse('Payment submitted..', safe=False)