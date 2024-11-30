# views.py
from django.shortcuts import render
# from .models import FeaturedPlace

def home_page(request):
    featured_places = [
        {"image": "images/featured-reo-de-janeiro-brazil.jpg", "name": "Rio De Janeiro, Brazil", "des": ""},
        {"image": "images/featured-north-bondi-australia.jpg", "name": "North Bondi, Australia", "des": ""},
        {"image": "images/featured-berlin-germany.jpg", "name": "Berlin, Germany", "des": ""},
        {"image": "images/featured-khwaeng-wat-arun-thailand.jpg", "name": "Khwaeng Wat Arun, Thailand"},
        {"image": "images/featured-rome-italy.jpg", "name": "Rome, Italy"},
        {"image": "images/featured-fuvahmulah-maldives.jpg", "name": "Fuvahmulah, Maldives"},
    ]
    # featured_places = FeaturedPlace.objects.all()  # Lấy tất cả địa điểm từ database
    return render(request, 'pages/home.html', {"featured_places": featured_places})

def gallery_page(request):
    gallery_places = [
    {"image": "images/popular-1.jpg", "name": "Eiffel Tower, Paris", "reviews": 400, "rating": 4.5, "des": "Lorem ipsum dolor sit amet consectetur adipisicing elit. Ducimus, quia!"},
    {"image": "images/popular-2.jpg", "name": "Machu Picchu, Peru", "reviews": 400, "rating": 4.5, "des": "Lorem ipsum dolor sit amet consectetur adipisicing elit. Ducimus, quia!"},
    {"image": "images/popular-3.jpg", "name": "Acropolis, Athens", "reviews": 400, "rating": 4.5, "des": "Lorem ipsum dolor sit amet consectetur adipisicing elit. Ducimus, quia!"},
    {"image": "images/popular-4.jpg", "name": "Bali, Indonesia", "reviews": 400, "rating": 4.5, "des": "Lorem ipsum dolor sit amet consectetur adipisicing elit. Ducimus, quia!"},
    {"image": "images/popular-5.jpg", "name": "Dubai, United Arab Emirates", "reviews": 400, "rating": 4.5, "des": "Lorem ipsum dolor sit amet consectetur adipisicing elit. Ducimus, quia!"},
    {"image": "images/popular-6.jpg", "name": "Bhutan", "reviews": 400, "rating": 4.5, "des": "Lorem ipsum dolor sit amet consectetur adipisicing elit. Ducimus, quia!"},
    {"image": "images/popular-7.jpg", "name": "Havana, Cuba", "reviews": 400, "rating": 4.5, "des": "Lorem ipsum dolor sit amet consectetur adipisicing elit. Ducimus, quia!"},
    {"image": "images/popular-8.jpg", "name": "Moskva, Russia", "reviews": 400, "rating": 4.5, "des": "Lorem ipsum dolor sit amet consectetur adipisicing elit. Ducimus, quia!"},
    ]
    gallery_window = [
    {"image": "images/gallery-1.jpg",},
    {"image": "images/gallery-2.jpg",},
    {"image": "images/gallery-3.jpg",},
    {"image": "images/gallery-4.jpg",},
    {"image": "images/gallery-5.jpg",},
    {"image": "images/gallery-6.jpg",},
    {"image": "images/gallery-7.jpg",},
    {"image": "images/gallery-8.jpg",},
    {"image": "images/gallery-9.jpg",},
    ]

    # return render(request, 'pages/gallery.html', {"gallery_places": gallery_places}, {"gallery_window": gallery_window})
    return render(request, 'pages/gallery.html', {"gallery_places": gallery_places,"gallery_window": gallery_window})

def contact_page(request):
    return render(request, 'pages/contact.html')
def about_page(request):
    return render(request, 'pages/about.html')