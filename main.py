# Main Menu:
# 1. Book Operations
# 2. User Operations
# 3. Author Operations
# 4. Genre Operations
# 5. Quit
from book import interface_books
from user import main as user
from author import main as author
from genre import main as genre
def menu():
    while True:
        user_input=input('''Main Menu:
                            1. Book Operations
                            2. User Operations
                            3. Author Operations
                            4. Genre Operations
                            5. Quit''')
        if user_input=="1":
            interface_books()
        elif user_input=="2":
            user()
        elif user_input=="3":
            author()
        elif user_input=="4":
            genre()
        elif user_input=="5":
            break
menu()
            