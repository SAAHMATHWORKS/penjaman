from django.urls import path
from django.conf.urls import *
from . import views

urlpatterns = [
    #Leave as empty string for base url
    path('', views.home, name="home"),
    path('contact.html', views.contact, name="contact"),
    url(r'^shop/(?P<id>\d+)-(?P<nom>.+)$', views.shop, name="shop"),
    url(r'^product/(?P<id>\d+)-(?P<slug>.+)$', views.details, name='singleDetail'),
    path('cart.html', views.cart, name="cart"),
    path('about.html', views.about, name="about"),
	path('checkout.html', views.checkout, name="checkout"),
    path('review.html', views.review, name="review"),
    path('update_item/', views.updateItem, name="update_item"),
	path('process_order/', views.processOrder, name="process_order"),
]