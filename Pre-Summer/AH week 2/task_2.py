#A Library holds books with data stored for each book as follows:

#RECORD Book:
#{
#	Title AS String
#	Author AS String
#	ISBN AS String
#        Price AS REAL
#}

#1.  Create a modular program in Python that will:

#a.  prompt the user to enter the Title, Author, ISBN and Price for a single book
#b.  store the details entered in a Python record
#c.  print the details of the book from the Python record

def def_class():
    class book():
        def __init__(self):
            self.title = str
            self.author = str
            self.isbn = str
            self.price = float

    bookList = [book() for i in range(10)]
    return bookList

def get_info(bookList):
    bookList[0].title = input("enter a title")
    bookList[0].author = input("enter an author")
    bookList[0].isbn = input("enter an ISBN")
    bookList[0].price = float(input("enter a price"))
    return bookList

def print_info(bookList):
    print(bookList[0].title)
    print(bookList[0].author)
    print(bookList[0].isbn)
    print(bookList[0].price)

bookList = def_class()
bookList = get_info(bookList)
print_info(bookList)
