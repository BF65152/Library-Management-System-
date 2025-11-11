from user import User
from book import Book

class Library:
    def __init__(self):
        self.list_of_books = []
        self.list_of_users = []
        self.list_of_available_books = []


    def add_book(self,book):
        self.list_of_books.append(book)
        return


    def add_user(self, user):
        self.list_of_users.append(user)
        return


#בדיקה אם המשתמש קיים ברשימה
    def find_user_by_id(self,user_id):
        for user in self.list_of_users:
            if user.id == user_id:
                return user
        return False


#אחרי שמוצאים את המשתמש בודקים עם הספר קיים ואז משאילים
    def borrow_book(self,book_isbn,user_id):
        user = self.find_user_by_id(user_id)
        for book in self.list_of_books:
            if book.isbn == book_isbn:
                print("your borrowed the book successfully")
                user.borrowed_books.append(book_isbn)
                book.is_available = False



#החזרת ספר עי בדיקה האם הושאל בכלל
    def return_book(self, user_id, book_isbn):
        user = self.find_user_by_id(user_id)
        for book in self.list_of_books:
            if book.is_available and book_isbn == book.isbn:
                print("the book is not borrowed")
            book.is_available = True

            #מסיר את הספר שהוחזר מהרשימה של הספרים המושאלים
            for u in user.borrowed_books:
                if u == book_isbn:
                    user.borrowed_books.remove(u)


#רשימה של ספרים שלא הושאלו
    def list_available_books(self):
        for book in self.list_of_books:
            if book.is_available:
                self.list_of_available_books.append(book)
        for j in self.list_of_available_books:
            print(j.__dict__)


    def search_book(self, title):
        for book in self.list_of_books:
            if title == book.title:
                print("the book exist")
            print("the book is not exist")


