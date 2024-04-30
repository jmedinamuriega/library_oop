# Book Operations:
# ```
# Book Operations:
# 1. Add a new book
# 2. Borrow a book
# 3. Return a book
# 4. Search for a book
# 5. Display all books

class Library:
    def __init__(self):
        self.books = []

    def add_book(self):
        title = input("Please introduce the title: ")
        author = input("Please introduce the author: ")
        isbn = input("Please introduce the ISBN: ")
        genre = input("Please introduce the genre: ")
        date = input("Please introduce the date: ")
        availability = "available"  
        book = {
            "title": title,
            "author": author,
            "ISBN": isbn,
            "genre": genre,
            "date": date,
            "availability": availability
        }
        self.books.append(book)
        print(f"Book '{title}' added successfully!")

    def borrow(self):
        borrowed_title = input("Please introduce the title of the borrowed book: ")
        for book in self.books:
            if book["title"] == borrowed_title:
                book["availability"] = "not available"
                print(f"Book '{borrowed_title}' marked as borrowed.")
                break
        else:
            print(f"Book '{borrowed_title}' not found in the library.")
        

    def return_book(self):
        returned_book=input("Please put the name of the returned book")
        for book in self.books:
            if book["title"] ==returned_book:
                book["availability"]="available"
                print(f"Book '{returned_book}' marked as available")
        else:
            print(f"Book '{returned_book}' not found in the library.")

    def search(self):
            search_title = input("Please introduce the title of the book you want to search for: ")
            for book in self.books:
                if book["title"] == search_title:
                    print(f"Book '{search_title}' found in the library.")
                    break
            else:
                print(f"Book '{search_title}' not found in the library.")
   
        

    def display(self):
        for book in self.books:
            print(f"Title: {book['title']}, Author: {book['author']}, Availability: {book['availability']}")

def interface_books():
    library = Library()
    while True:
        user_input = input('''Book Operations:
                            1. Add a new book
                            2. Borrow a book
                            3. Return a book
                            4. Search for a book
                            5. Display all books
                            6. Leave
                            Enter your choice: ''')
        if user_input == "1":
            library.add_book()
        elif user_input == "2":
            library.borrow()
        elif user_input == "3":
            library.return_book()
        elif user_input == "4":
            library.search()
        elif user_input == "5":
            library.display()
        elif user_input == "6":
            break
        else:
            print("Please enter a valid number!")

