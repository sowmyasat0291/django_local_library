class Book:
    def __init__(self, title, author, book_id):  # Initialize a Book object with title, author, and book ID.
        self.title = title  # Set the title of the book.
        self.author = author  # Set the author of the book.
        self.book_id = book_id  # Set the unique book ID.
        self.available = True  # Initialize the book as available for borrowing.

    def __str__(self):  # Return a string representation of the book.
        return f"{self.title} by {self.author} (ID: {self.book_id})"

    def check_availability(self):  # Check if the book is available for borrowing.
        return self.available  # Return True if available, False otherwise.

    def borrow_book(self):  # Attempt to borrow the book.
        if self.available:  # If the book is available:
            self.available = False  # Mark the book as not available.
            return True  # Return True to indicate successful borrowing.
        else:  # If the book is not available:
            return False  # Return False to indicate unsuccessful borrowing.

    def return_book(self):  # Return the book.
        self.available = True  # Mark the book as available again.
