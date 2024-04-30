# Author Operations:
# ```
# Author Operations:
# 1. Add a new author
# 2. View author details
# 3. Display all authors
class Author:
    def __init__(self, name, biography, authors=None):
        self.author = {"name": name,
                       "biography": biography,
                       "authors": authors or []}

    def add_author(self, new_author_name, new_author_biography):
        new_author = Author(name=new_author_name, biography=new_author_biography)
        return new_author

    def view_details(self, author_name):
        if self.author["name"] == author_name:
            print(f"Author Details for {author_name}:")
            print(f"Biography: {self.author['biography']}")
        else:
            print(f"Author '{author_name}' not found.")

def main():
    authors = []
    while True:
        user_decision = input('''Author Operations:
                               1. Add a new author
                               2. View author details
                               3. Display all authors
                               4. Exit\n''')
        if user_decision == "1":
            new_author_name = input("Enter the author's name: ")
            new_author_biography = input("Enter the author's biography: ")
            authors.append(Author(name=new_author_name, biography=new_author_biography))
        elif user_decision == "2":
            author_name = input("Please enter the author's name: ")
            for author in authors:
                author.view_details(author_name)
        elif user_decision == "3":
            print("All Authors:")
            for author in authors:
                print(f"{author.author['name']} (Biography: {author.author['biography']})")
        elif user_decision == "4":
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
