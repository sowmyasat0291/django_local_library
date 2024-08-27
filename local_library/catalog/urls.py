from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('', views.home_view, name='home'),  # Maps the root URL to home_view
    path('about/', views.about_view, name='about'),  # Maps /about/ URL to about_view
]
