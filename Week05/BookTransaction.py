from collections import defaultdict
import time
bookdic = {}
class Books:
    bookList = []
    def __init__(self,name,author,instore):
        Books.bookList.append(name)
        self.instore = instore
        self.name = name
        self.author = author
    def display(self):
        for book in Books.bookList:
            print(f"Book Title: {book.name}\nAuthor: {book.author}")

class Transaction:
    transactionReport = []
    def __init__(self,date,book) -> None:
        assert book in Books.bookList, "Book Not found!"
        self.book = book
        self.date = date
    def display(self):
        for data in Transaction.transactionReport:
            print(f"Book Title: {data[1]} Date: {data[2]}")
    def checkin(self,book):
        book.instore = True
    def checkout(self,book):
        if book.instore:
            self.user.add_book(self.book)
            Transaction.transactionReport.append([self.book,self.date])
            self.book.instore = False
        else:
            print("Book Currently Not in store :(")
class User:
    usersList = []
     
    def __init__(self,name,phone):
        User.usersList.append([name,phone])
        self.name = name
        self.phone = phone
        self.books = []
    def display(self):
        print(f"Name: {self.name}\nPhone: {self.phone}")
        for book in self.books:
            print(f"Book Title: {book.name}\nAuthor: {book.author}")
    def add_book(self,book):
        self.books.append(book)
        

def main():
    while True:
        print(f"******WELCOME TO MY BOOK STORE*******\n")
        print(f"1.Register User\n")
        print(f"2.Register Book\n")
        print(f"3.Checkout Book\n")
        print(f"4.Checkin Book\n")
        print(f"5.See Transaction History\n")
        print(f"6.See User List\n")
        choice = int(input())
        if choice == 1:
            print("Please Enter Name: ",end = '')
            name = input()
            print("Please Enter Phone Number: ",end = '')
            phone = input()
            user1 = User(name,phone)
        elif choice == 2:
            print("Please Enter Book Title: ",end = '')
            name = input()
            print("Please Enter Book Author: ",end = '')
            author = input()
            book1 = Books(name,author,True) 
            bookdic[name] = book1
        elif choice == 3:
            print("Please Enter Book Title: ",end = '')
            name = input()
            if name in bookdic:
                Transaction.checkout(bookdic[name])
            else:
                print("Book Not from this library.")
        elif choice == 4:
            print("Please Enter Book Title: ",end = '')
            name = input()
            if name in bookdic:
                transaction1 = Transaction(time.strftime("[%Y-%m-%d %H:%M:%S]"),bookdic[name])
                
            else:
                print("Book Not Found :(")
        elif choice == 5:
            print("**TRANSACTION HISTORY**")
            for t in Transaction.transactionReport:
                print(t)
            

        elif choice == 6:
            print("**User List**")
            for t in User.usersList:
                print(t)
        elif choice == 7:
            print("Exiting Program...")
            break


if __name__ == "__main__":
    main()

