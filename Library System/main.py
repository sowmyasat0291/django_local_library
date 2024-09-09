# main.py
from library import Library
from book import Book
from member import Member

def main():
    # Create Library object
    library_name = input("Enter library name: ")
    library = Library(library_name)

    # Add some books to the library
    book1 = Book("Harry Potter", "J.K. Rowling", 1)
    book2 = Book("Lord of the Rings", "J.R.R. Tolkien", 2)
    library.add_book(book1)
    library.add_book(book2)

    # Add some members to the library
    member1 = Member("Alice", 101)
    member2 = Member("Bob", 102)
    library.add_member(member1)
    library.add_member(member2)

    while True:  # Loop until user decides to log out.
        current_member = library.authenticate_member()  # Authenticate or create a new member.

        if current_member is None:  # If user chooses to exit the login page.
            break  # Exit the program.

        while True:  # Loop for the member's session.
            print(f"\n===== Library Management System - Welcome {current_member.name} =====")
            print("1. Display all books")
            print("2. Display all members")
            print("3. Borrow a book")
            print("4. Return a book")
            print("5. Add a new book")
            print("6. Logout")
            
            choice = input("Enter your choice (1-6): ")

            if choice == '1':  # If user chooses to display all books:
                library.display_books()  # Display all books in the library.
            elif choice == '2':  # If user chooses to display all members:
                library.display_members()  # Display all members of the library.
            elif choice == '3':  # If user chooses to borrow a book:
                try:
                    book_id = int(input("Enter the book ID you want to borrow: "))  # Prompt for book ID.
                    book = next((b for b in library.books if b.book_id == book_id), None)  # Find book by ID.
                    if book:  # If book exists:
                        if current_member.borrow_book(book):  # Attempt to borrow the book.
                            print(f"Book '{book.title}' borrowed successfully.")  # Print success message.
                        else:
                            print(f"Book '{book.title}' is not available.")  # Print unavailable message.
                    else:
                        print("Invalid book ID.")  # Print invalid ID message.
                except ValueError:
                    print("Invalid input. Please enter a valid integer for book ID.")  # Handle invalid input.
            elif choice == '4':  # If user chooses to return a book:
                try:
                    book_id = int(input("Enter the book ID you want to return: "))  # Prompt for book ID.
                    book = next((b for b in library.books if b.book_id == book_id), None)  # Find book by ID.
                    if book:  # If book exists:
                        if book in current_member.borrowed_books:  # Check if the book is borrowed by the member.
                            current_member.return_book(book)  # Return the book.
                            print(f"Book '{book.title}' returned successfully.")  # Print success message.
                        else:
                            print(f"You haven't borrowed '{book.title}'.")  # Print not borrowed message.
                    else:
                        print("Invalid book ID.")  # Print invalid ID message.
                except ValueError:
                    print("Invalid input. Please enter a valid integer for book ID.")  # Handle invalid input.
            elif choice == '5':  # If user chooses to add a new book:
                try:
                    title = input("Enter the book title: ")  # Prompt for book title.
                    author = input("Enter the author: ")  # Prompt for author.
                    book_id = max([book.book_id for book in library.books], default=0) + 1  # Generate new book ID.
                    new_book = Book(title, author, book_id)  # Create new book object.
                    library.add_book(new_book)  # Add the new book to the library.
                    print(f"Book '{title}' added successfully with ID {book_id}.")  # Print success message.
                except Exception as e:
                    print(f"Error adding book: {e}")  # Print error message if adding fails.
            elif choice == '6':  # If user chooses to log out:
                print("Logging out...")  # Print logging out message.
                return  # Break the inner loop to log out.
            else:
                print("Invalid choice. Please enter a number from 1 to 5.")  # Handle invalid menu choice.

if __name__ == "__main__":
    main()  # Call main function to start the program.
