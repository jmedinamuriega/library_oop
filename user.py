class Users:
    def __init__(self, name, libraryID, books=None):
        self.user = {"name": name,
                     "libraryID": libraryID,
                     "books": books or []}

    def add_user(self, new_user_name, new_user_libraryID):
        new_user = Users(name=new_user_name, libraryID=new_user_libraryID)
        return new_user

    def view_details(self, user_name):
        if self.user["name"] == user_name:
            print(f"User Details for {user_name}:")
            print(f"Library ID: {self.user['libraryID']}")
            print(f"Books borrowed: {', '.join(self.user['books'])}")
        else:
            print(f"User '{user_name}' not found.")

def main():
    users = []
    while True:
        user_decision = input('''1. Add a new user
                               2. View user details
                               3. Display all users
                               4. Exit\n''')
        if user_decision == "1":
            new_user_name = input("Enter the user's name: ")
            new_user_libraryID = input("Enter the user's library ID: ")
            users.append(Users(name=new_user_name, libraryID=new_user_libraryID))
        elif user_decision == "2":
            user_name = input("Please enter the user's name: ")
            for user in users:
                user.view_details(user_name)
        elif user_decision == "3":
            print("All Users:")
            for user in users:
                print(f"{user.user['name']} (Library ID: {user.user['libraryID']})")
        elif user_decision == "4":
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
