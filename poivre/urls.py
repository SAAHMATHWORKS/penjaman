from django.urls import path
from . import views

urlpatterns = [
    #Leave as empty string for base url
    path('', views.home, name="home"),
    path('contact.html', views.contact, name="contact"),
    path('shop.html', views.store, name="shop"),
    path('cart.html', views.cart, name="cart"),
	path('checkout.html', views.checkout, name="checkout"),
    path('update_item/', views.updateItem, name="update_item"),
	path('process_order/', views.processOrder, name="process_order"),
]