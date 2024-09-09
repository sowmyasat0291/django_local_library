class Member:
    def __init__(self, name, member_id):  # Initialize a Member object with name and member ID.
        self.name = name  # Set the name of the member.
        self.member_id = member_id  # Set the unique member ID.
        self.borrowed_books = []  # Initialize an empty list to keep track of borrowed books.

    def __str__(self):  # Return a string representation of the member.
        return f"{self.name} (ID: {self.member_id})"

    def borrow_book(self, book):  # Attempt to borrow a book.
        if book.check_availability():  # If the book is available:
            self.borrowed_books.append(book)  # Add the book to the member's borrowed books.
            book.borrow_book()  # Mark the book as borrowed.
            return True  # Return True to indicate successful borrowing.
        else:  # If the book is not available:
            return False  # Return False to indicate unsuccessful borrowing.

    def return_book(self, book):  # Return a borrowed book.
        if book in self.borrowed_books:  # If the book is in the member's borrowed books:
            self.borrowed_books.remove(book)  # Remove the book from the borrowed books list.
            book.return_book()  # Mark the book as returned.
