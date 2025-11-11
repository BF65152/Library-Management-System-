test


b1 = Book("pop","moshe",11,True)
b2 = Book("sps","david",12,True)
u1 = User("chaim",123456)

library = Library()
library.add_user(u1)

library.add_book(b1)
library.add_book(b2)


library.borrow_book(11,123456)
library.borrow_book(12,123456)

for i in library.list_of_books:
    print(i.__dict__)

library.list_available_books()
print(u1.borrowed_books)

library.return_book(123456,11)
library.return_book(123456,12)
# #
print(u1.borrowed_books)