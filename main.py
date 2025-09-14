#different classes: Book, User, Library. Lastly we need a main function

class Book:
    def ___init__(self, name, author, genre, page_number, status):
        self.name = name
        self.author = author
        self.genre = genre
        self.page_number = page_number
        self.status = status


class User:
    def __init__(self, name):
        self.name = name
        self.books = []

    #method to return a book 
    def return_book(self, bookName):
        self.bookName = bookName




    #method to borrow a book
    def borrow_book(self, bookName):
        self.bookName = bookName

 

class Library:
    def __init__(self, name):
        self.name = name
        
