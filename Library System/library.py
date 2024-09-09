from book import Book
from member import Member

class Library:
    def __init__(self, name):  # Initialize a Library object with a name.
        self.name = name  # Set the name of the library.
        self.books = []  # Initialize an empty list to store books in the library.
        self.members = {}  # Initialize a dictionary to store members of the library.

    def add_book(self, book):  # Add a book to the library.
        self.books.append(book)  # Append the book to the library's list of books.

    def add_member(self, member):  # Add a member to the library.
        self.members[member.member_id] = member  # Add the member to the dictionary with member ID as key.

    def display_books(self):  # Display all books in the library.
        if not self.books:  # If there are no books in the library:
            print("No books in the library.")  # Print a message indicating no books are available.
        else:  # If there are books in the library:
            print("Books available in the library:")  # Print a header indicating available books.
            for book in self.books:  # Iterate through each book in the library:
                print(book)  # Print the string representation of each book.

    def display_members(self):  # Display all members of the library.
        if not self.members:  # If there are no members in the library:
            print("No members in the library.")  # Print a message indicating no members are registered.
        else:  # If there are members in the library:
            print("Library members:")  # Print a header indicating library members.
            for member in self.members.values():  # Iterate through each member in the library:
                print(member)  # Print the string representation of each member.

    def authenticate_member(self):  # Authenticate or create a new member.
        while True:  # Loop until a valid member is authenticated or created.
            print("\n===== Library Authentication =====")
            print("1. Login")
            print("2. Create new account")
            print("3. View existing users")
            print("4. Exit")
            choice = input("Enter your choice (1-4): ")
            if choice == '1':  # If user chooses to log in:
                try:
                    member_id = int(input("Enter your member ID: "))  # Prompt for member ID.
                    if member_id in self.members:  # Check if member ID exists.
                        print(f"Welcome, {self.members[member_id].name}!")  # Print welcome message.
                        return self.members[member_id]  # Return the member object.
                    
                    else:
                        print("Member ID not found. Please try again.")  # Print error message.
                except ValueError:
                    print("Invalid input. Please enter a valid integer for member ID.")  # Handle invalid input.
            elif choice == '2':  # If user chooses to create a new account:
                name = input("Enter your name: ")  # Prompt for name.
                new_id = max(self.members.keys(), default=100) + 1  # Generate new member ID.
                new_member = Member(name, new_id)  # Create new member object.
                self.add_member(new_member)  # Add new member to the library.
                print(f"Account created successfully! Your member ID is {new_id}.")  # Print success message.
                return new_member  # Return the new member object.
            elif choice == '3':  # If user chooses to view existing users:
                self.display_members()  # Display existing members.
            elif choice == '4':  # If user chooses to exit:
                print("Exiting login page. Goodbye!")  # Print exit message.
                return None  # Return None to exit.
            else:
                print("Invalid choice. Please enter a number from 1 to 4.")  # Handle invalid menu choice.
