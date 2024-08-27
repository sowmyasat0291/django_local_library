from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('books/', views.BookListView.as_view(), name='books'),
    path('book/<int:pk>', views.BookDetailView.as_view(), name='book-detail'),
    path('author/<int:pk>/', views.author_detail, name='author-detail'),



    #path('', views.home_view, name='home'),  # Maps the root URL to home_view
    #path('about/', views.about_view, name='about'),  # Maps /about/ URL to about_view
]
