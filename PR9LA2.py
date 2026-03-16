class Book:

    def __init__(self, name):
        self.name = name
        self.issued = False


class Library:

    def __init__(self):
        self.books = []

    def addBook(self):
        name = input("Enter Book Name: ")
        book = Book(name)
        self.books.append(book)
        print("Book Added Successfully")

    def showBooks(self):
        print("\nAvailable Books:")
        for b in self.books:
            print(b.name)

    def issueBook(self):
        name = input("Enter Book Name to Issue: ")

        for b in self.books:
            if b.name == name and not b.issued:
                b.issued = True
                print("Book Issued")
                return

        print("Book Not Available")

    def returnBook(self):
        name = input("Enter Book Name to Return: ")

        for b in self.books:
            if b.name == name and b.issued:
                b.issued = False
                print("Book Returned")
                return

        print("Invalid Book Name")


lib = Library()

while True:

    print("\n1 Add Book")
    print("2 Show Books")
    print("3 Issue Book")
    print("4 Return Book")
    print("5 Exit")

    ch = int(input("Enter Choice: "))

    if ch == 1:
        lib.addBook()

    elif ch == 2:
        lib.showBooks()

    elif ch == 3:
        lib.issueBook()

    elif ch == 4:
        lib.returnBook()

    elif ch == 5:
        print("Thank You")
        break

    else:
        print("Invalid Choice")