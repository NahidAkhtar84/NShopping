from django.contrib import admin
from django.urls import path
from .views import home, signup, login, basket, singlepropa, search, products, coupon, aboutus
from .middleware.auth import auth_middleware
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from orders.views import checkout, orders, add_user_address
from marketing.views import dismiss_marketing, email_signup


urlpatterns = [
    path('', home.Index.as_view(), name='homepage'),
    path('products', products.Products.as_view(), name='products'),
    path('signup', signup.SignUp.as_view(), name="signup"),
    path('login', login.Login.as_view(), name="login"),
    path('logout', login.logout , name="logout"),
    path('basket', basket.Basket.as_view() , name="basket"),
    path('coupon', basket.Basket.as_view(), name="coupon"),
    path('singlepropa/<str:slug>', singlepropa.SinglePropa.as_view() , name="singlepropa"),
    path('s/', search.Search.as_view() , name="search"),
    path('add_to_cart/<str:slug>', basket.add_to_cart , name="add_to_cart"),
    path('remove_from_cart/<int:id>', basket.remove_from_cart , name="remove_from_cart"),
    path('checkout', auth_middleware(checkout), name="checkout"),
    path('orders', orders, name="orders"),
    path('ajax/dismiss_marketing', dismiss_marketing, name="dismiss_marketing"),
    path('ajax/email_signup', email_signup, name="ajax_email_signup"),
    path('ajax/add_user_address', add_user_address, name="ajax_add_user_address"),
    path('orderproceed', checkout, name="orderproceed"),
    path('aboutus/<str:tabinfo>', aboutus.AboutUs.as_view(), name="aboutus"),

]
