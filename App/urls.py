from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home'),
    path('gallery', views.gallery_page, name='gallery'),
    path('contact', views.contact_page, name='contact'),
    path('about', views.about_page, name='about'),
]
