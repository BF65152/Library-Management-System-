class Book:
    def __init__(self,title,author,isbn,is_available):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_available = is_available

    def maybe__str__(self):
        print(f"the book: {self.title},id {self.isbn}, his author: {self.author}, is available? {self.is_available}")