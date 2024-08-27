from django.shortcuts import render
#from django.http import HttpResponse
from django.views import generic
from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Book, Author, BookInstance, Genre

def author_detail(request, pk):
    author = get_object_or_404(Author, pk=pk)
    return render(request, 'catalog/author_detail.html', {'author': author})

def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()

    # Available books (status = 'a')
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()

    # The 'all()' is implied by default.
    num_authors = Author.objects.count()
    # Number of visits to this view, as counted in the session variable.
    num_visits = request.session.get('num_visits', 0)
    num_visits += 1
    request.session['num_visits'] = num_visits

    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
        'num_visits': num_visits,

    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)

"""
def home_view(request):
    return HttpResponse("Welcome to the home page!")

def about_view(request):
    return HttpResponse("This is the about page.")
"""
# Create your views here.
class BookListView(generic.ListView):
    model = Book
    paginate_by = 2
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get the context
        context = super(BookListView, self).get_context_data(**kwargs)
        # Create any data and add it to the context
        context['some_data'] = 'This is just some data'
        return context
class BookDetailView(generic.DetailView):
    model = Book
    def book_detail_view(request, primary_key):
     book = get_object_or_404(Book, pk=primary_key)
     return render(request, 'catalog/book_detail.html', context={'book': book})
class AuthorListView(ListView):
    model = Author
    template_name = 'catalog/author_list.html'  # Optional: specify your template
    context_object_name = 'author_list'  # Optional: name to use in the template
    paginate_by = 10  # Optional: add pagination if you have many authors
class AuthorDetailView(DetailView):
    model = Author
    template_name = 'catalog/author_detail.html'  # Optional: specify your template
    context_object_name = 'author'  # Optional: name to use in the template


