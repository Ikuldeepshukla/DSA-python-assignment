# Define a class Book with instance object variables bookid, title and price. Initialize them via __init__() method. Also define method to show book variables.

class Book:
    def __init__(self, bookId, title, price):
        self.bookId = bookId
        self.title = title
        self.price = price

    def show(self):
        print('Book Id: ', self.bookId)
        print('Title: ', self.title)
        print('Price: ', self.price)

# initialize object
b1 = Book(1, 'Python', 300)
b2 = Book(2, 'Java', 500)
b3 = Book(3, 'C++', 700)

b1.show()
b2.show()
b3.show()
