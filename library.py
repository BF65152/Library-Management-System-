class Library:
    def __init__(self, list_of_books, list_of_users):
        self.list_of_books = []
        self.list_of_users = []

    def add_book(self, book):
        self.list_of_books.append(book)
        return

    def add_user(self, user):
        self.list_of_users.append(user)
        return

    def borrow_book(self, user_id, book_isbn):
        for book in self.list_of_books:
            if book.ISBN == book_isbn:
                book.is_available = False
                for user in self.list_of_users:
                    if user.id == user_id:
                        user.borrowed_books.append(book)


    def return_book(self, user_id, book_isbn):
        return_ = [user_id, book_isbn]
        return return_

    def list_available_books(self):
        pass

    def search_book(self, title):
        pass
