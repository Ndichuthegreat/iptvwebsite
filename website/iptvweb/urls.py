from django.urls import path
from . import views

urlpatterns = [
   path('',views.home, name="home"),
   path('about.html',views.about, name="about"),
   path('subscribe.html',views.subscribe, name="subscribe"),
   path('contact.html',views.contact, name="contact"),


]