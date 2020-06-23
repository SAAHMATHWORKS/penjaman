from django.urls import path
from django.conf.urls import *
from . import views

urlpatterns = [
    #Leave as empty string for base url
    path('', views.home, name="home"),
    path('contact.html', views.contact, name="contact"),
    path('shop.html', views.store, name="shop"),
    url(r'^product/(?P<id>\d+)$', views.details, name='singleDetail'),
    path('cart.html', views.cart, name="cart"),
	path('checkout.html', views.checkout, name="checkout"),
    path('update_item/', views.updateItem, name="update_item"),
	path('process_order/', views.processOrder, name="process_order"),
]