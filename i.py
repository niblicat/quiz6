from dataclasses import dataclass
# Interface Segregation Pricnciple

@dataclass
class Book:
    id: int
    title: str
    author: str
    genre: str
    
@dataclass
class Library:
    books: list[Book]
    location: str
@dataclass
class User:
    id: int
    name: str
    address: str
class ManagementPermissions():
    def add_book(self, book: Book):
        print("added", book, "to the catalog")
    def remove_book(self, book: Book):
        print("removed", book, "from the catalog")
class StatisticsPermissions():
    def print_overdue_books_report(self, location: str):
        print("printed overdue report at", location)
    def print_borrowings_report(self, location: str):
        print("printed borrowings report at", location)
    def print_popularity_report(self, location: str):
        print("printed book popularity report at", location)
class BorrowPermissions():
    def borrow_book(self, book: str):
        print("borrowing", book)
class ReturnPermissions():
    def return_book(self, book: str):
        print("returning", book)
class SearchPermissions():
    def title_search(self, query: str):
        print("searching for books by title", query)
    def author_search(self, query: str):
        print("searching for books by author", query)
    def genre_search(self, query: str):
        print("searching for books by genre", query)
        
class Guest(User, SearchPermissions):
    def __init__(self, id, name, address):
        super().__init__(id, name, address)
        print("created guest")
class ProbationMember(User, SearchPermissions, ReturnPermissions):
    def __init__(self, id, name, address):
        super().__init__(id, name, address)
        print("created member on probation (not advised)")
class Member(User, SearchPermissions, BorrowPermissions, ReturnPermissions):
    def __init__(self, id, name, address):
        super().__init__(id, name, address)
        print("created member")
class Librarian(User, SearchPermissions, BorrowPermissions, ReturnPermissions, ManagementPermissions):
    def __init__(self, id, name, address):
        super().__init__(id, name, address)
        print("created librarian")
class Admin(User, SearchPermissions, BorrowPermissions, ReturnPermissions, ManagementPermissions, StatisticsPermissions):
    def __init__(self, id, name, address):
        super().__init__(id, name, address)
        print("created admin")


def main() -> None:
    sam = Member(id=0, name="sam", address="the street")
    print(sam.__repr__())
    jam = Librarian(id=1, name="jam", address="the house over there")
    print(jam.__repr__())
    
    sam.genre_search("rock")
    
    jam.add_book(Book(1234, "Viking History", "Sleekingorgon", "nonfiction"))

if __name__ == "__main__":
    main()