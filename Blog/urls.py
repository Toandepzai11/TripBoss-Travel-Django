from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='blog'),
    path('<int:id>/', views.post_detail, name='post_detail'),
    path('create/', views.create_post, name='create_post'),
]
