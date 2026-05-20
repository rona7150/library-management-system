class Book:
    def __init__(self, book_id: str, title: str, author: str):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.available = True

    def borrow(self):
        self.available = False

    def return_book(self):
        self.available = True

    def __str__(self):
        status = "Available" if self.available else "Borrowed"
        return f"{self.book_id} - {self.title} by {self.author} [{status}]"

class Member:
    def __init__(self, member_id: str, name: str, email: str):
        self.member_id = member_id
        self.name = name
        self.email = email

    def __str__(self):
        return f"{self.member_id} - {self.name} ({self.email})"

class Loan:
    def __init__(self, loan_id: str, book: Book, member: Member):
        self.loan_id = loan_id
        self.book = book
        self.member = member
        self.is_active = True

    def __str__(self):
        status = "Active" if self.is_active else "Closed"
        return f"{self.loan_id} - {self.member.name} borrowed {self.book.title} [{status}]"