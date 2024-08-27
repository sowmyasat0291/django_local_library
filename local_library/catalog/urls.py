from django.urls import path
from . import views
from .views import BookListView, BookDetailView, AuthorListView, AuthorDetailView


urlpatterns = [
    path('', views.index, name='index'),
    path('books/', views.BookListView.as_view(), name='books'),
    path('book/<int:pk>', views.BookDetailView.as_view(), name='book-detail'),
    path('authors/', views.AuthorListView.as_view(), name='authors'),
    path('author/<int:pk>',
         views.AuthorDetailView.as_view(), name='author-detail'),
    path('books/', BookListView.as_view(), name='book-list'),
    path('mybooks/', views.LoanedBooksByUserListView.as_view(), name='my-borrowed'),




    #path('', views.home_view, name='home'),  # Maps the root URL to home_view
    #path('about/', views.about_view, name='about'),  # Maps /about/ URL to about_view
]
