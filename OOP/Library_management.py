class LibraryBook:
    def __init__(self,title ,author,book_id):
     self.title = title
     self.author = author
     self.book_id = book_id
     self.available = True

    def issue_book(self):
        if self.available:
            self.available = False
            print(self.title,"has been issued.")
        else:
         print(self.title, " is not available")
    def return_book(self):
        if not self.available:
            self.available = True
            print(self.title,"has beem returned.")
        else:
            print(self.title, "is already available ")

    def display_info(self):
            print("Title:", self.title)
            print("Author:",self.author)
            print("Book ID:", self.book_id)
            print("Available:",self.available)
            print("-------------")

book1 = LibraryBook("Python Basics", "Ali",101)
book2 = LibraryBook("Data Science", "Ahmed", 102)
book3 = LibraryBook("Artificial Intelligence", "Sara", 103)
book4 = LibraryBook("C++ programming","Usman", 104)
book1.display_info()
book1.issue_book()
book1.issue_book()
book1.return_book()

book2.issue_book()
book3.return_book()
book4.display_info()

