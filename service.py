from exceptions import BookNotFoundError, MemberNotFoundError, BookUnavailableError, LoanNotFoundError
from models import Book, Member, Loan

class LibraryService:
    def __init__(self):
        self._books = {}
        self._members = {}
        self._loans = []
        self._loan_counter = 0

    def add_book(self, book_id: str, title: str, author: str) -> Book:
        book = Book(book_id, title, author)
        self._books[book.book_id] = book
        return book

    def register_member(self, member_id: str, name: str, email: str) -> Member:
        member = Member(member_id, name, email)
        self._members[member.member_id] = member
        return member

    def borrow_book(self, book_id: str, member_id: str) -> Loan:
        book = self._books.get(book_id)
        if book is None:
            raise BookNotFoundError("Book not found.")
        
        member = self._members.get(member_id)
        if member is None:
            raise MemberNotFoundError("Member not found.")
        
        if not book.available:
            raise BookUnavailableError("Book is already borrowed.")
        
        self._loan_counter += 1
        loan_id = f"L{self._loan_counter:03d}"
        loan = Loan(loan_id, book, member)
        self._loans.append(loan)
        book.borrow()
        return loan

    def return_book(self, book_id: str) -> Book:
        book = self._books.get(book_id)
        if book is None:
            raise BookNotFoundError("Book not found.")
        if book.available:
            raise BookUnavailableError("Book is already in the library inventory.")
        
        active_loan = next(
            (loan for loan in self._loans if loan.book_id == book_id and loan.is_active), 
            None
        )
        if active_loan:
            active_loan.is_active = False
            book.return_book()
            return book
        else:
            raise LoanNotFoundError("No active loan found for this book.")

    def view_books(self) -> list:
        return list(self._books.values())

    def view_members(self) -> list:
        return list(self._members.values())

    def view_loans(self) -> list:
        return self._loans