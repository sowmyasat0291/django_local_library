from django.urls import path
from . import views
from .views import BookListView, BookDetailView, AuthorListView, AuthorDetailView


urlpatterns = [
    path('', views.index, name='index'),
    path('books/', BookListView.as_view(), name='book-list'),  # Use a single entry for the books list view
    path('book/<int:pk>/', BookDetailView.as_view(), name='book-detail'),
    path('authors/', AuthorListView.as_view(), name='author-list'),
    path('author/<int:pk>/', AuthorDetailView.as_view(), name='author-detail'),



    #path('', views.home_view, name='home'),  # Maps the root URL to home_view
    #path('about/', views.about_view, name='about'),  # Maps /about/ URL to about_view
]
