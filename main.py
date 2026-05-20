import sys
from service import LibraryService
from exceptions import BookNotFoundError, MemberNotFoundError, BookUnavailableError, LoanNotFoundError

def print_menu():
    print("\n==============================")
    print(" LIBRARY MANAGEMENT SYSTEM")
    print("==============================")
    print("1. Add Book")
    print("2. Register Member")
    print("3. Borrow Book")
    print("4. Return Book")
    print("5. View Books")
    print("6. View Members")
    print("7. View Loans")
    print("8. Exit")
    print("==============================")

def main():
    service = LibraryService()
    while True:
        print_menu()
        choice = input("Enter choice (1-8): ").strip()

        if choice == "1":
            print("\n--- Add New Book ---")
            book_id = input("Input Book ID: ").strip()
            title = input("Input Book Title: ").strip()
            author = input("Input Book Author: ").strip()
            book = service.add_book(book_id, title, author)
            print(f"Book added: {book}")

        elif choice == "2":
            print("\n--- Register New Member ---")
            member_id = input("Input Member ID: ").strip()
            name = input("Input Member Name: ").strip()
            email = input("Input Member Email: ").strip()
            member = service.register_member(member_id, name, email)
            print(f"Member registered: {member}")

        elif choice == "3":
            print("\n--- Borrow a Book ---")
            book_id = input("Input Book ID: ").strip()
            member_id = input("Input Member ID: ").strip()
            try:
                loan = service.borrow_book(book_id, member_id)
                print(f"{loan}")
            except (BookNotFoundError, MemberNotFoundError, BookUnavailableError) as error:
                print(f"Output: {error}")

        elif choice == "4":
            print("\n--- Return a Book ---")
            book_id = input("Input Book ID to Return: ").strip()
            try:
                book = service.return_book(book_id)
                print(f"Success: {book.title} has been successfully returned.")
            except (BookNotFoundError, BookUnavailableError, LoanNotFoundError) as error:
                print(f"Output: {error}")

        elif choice == "5":
            print("\n--- Library Books Inventory ---")
            books = service.view_books()
            if not books:
                print("No books found.")
            else:
                print("Books:")
                for book in books:
                    print(book)

        elif choice == "6":
            print("\n--- Registered Members ---")
            members = service.view_members()
            if not members:
                print("No members found.")
            else:
                print("Members:")
                for member in members:
                    print(member)

        elif choice == "7":
            print("\n--- Loan Transactions Registry ---")
            loans = service.view_loans()
            if not loans:
                print("No loans found.")
            else:
                print("Loans:")
                for loan in loans:
                    print(loan)

        elif choice == "8":
            print("Program closed.")
            sys.exit(0)
        else:
            print("Invalid Choice. Please enter a number between 1 and 8.")

if __name__ == "__main__":
    main()