class Genre:
    def __init__(self, name, genre, genres=None):
        self.genre = {"name": name,
                      "genre": genre,
                      "genres": genres or []}

    def add_genre(self, new_genre_name):
        new_genre = Genre(name=new_genre_name, genre="") 
        return new_genre

    def view_details(self, genre):
        if self.genre["name"] == genre:
            print(f"Genre Details for {genre}:")
        else:
            print(f"Genre '{genre}' not found.")

def main():
    genres = []
    while True:
        user_decision = input('''Genre Operations:
                               1. Add a new genre
                               2. View genre details
                               3. Display all genres
                               4. Exit\n''')
        if user_decision == "1":
            new_genre_name = input("Enter the genre's name: ")
            genres.append(Genre(name=new_genre_name, genre=""))  
        elif user_decision == "2":
            genre_name = input("Please enter the genre's name: ")
            for genre in genres:
                genre.view_details(genre_name)  
        elif user_decision == "3":
            print("All Genres:")
            for genre in genres:
                print(f"{genre.genre['name']}")  
        elif user_decision == "4":
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
