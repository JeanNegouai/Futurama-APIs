import requests

# Fetch data from the API
response = requests.get("https://api.sampleapis.com/playstation/games")

# Convert JSON data to Python list of dictionaries
games = response.json()

def games_genre():

    # Create a set to store unique genres
    original_set = set() # Can I switch this to a regular list since I check the uniqueness on line 23/26

    # Create a dictionary to store genres and their corresponding game names
    genre_to_games = {}




    # Iterate over each game
    for game in games:
        
        # Use 'get' to access the genre list and retrieve values associated with 'genre' in the dictionary
            genres = game.get("genre", [])
            game_name = game.get("name") # Retrieves all of the games name

        # Check if the genres list is empty, if not skip the game 
            if len(genres) == 0:
                 continue
        
            # Add each genre to the "original_set" set to ensure uniqueness
            for genre in genres:
                if genre:
                    genre_lower = genre.lower()
                    original_set.add(genre_lower)
                    if genre_lower not in genre_to_games: # If genre not in dictionary "genre_to_games = {}"
                        genre_to_games[genre_lower] = [] # prepares a space to store game names that belong to that specific genre. 
                genre_to_games[genre_lower].append(game_name) # result (example): "role playing": [MGS1]
                    

                   

    # Print unique genres
    for genre in original_set:
        print(genre)


        # Prompt user for a genre
    user_genre = input("Enter a genre to see the games: ").strip().lower()

        # Show games for the entered genre
    if user_genre in genre_to_games:
            print(f"Games in the genre '{user_genre}':")
            for game in genre_to_games[user_genre]:
                print(f"- {game}")
    else:
        print(f"No games found for the genre '{user_genre}'.")


def user_choice():
    while True:
        user_selection = input('Press 1 to view playstation game genres, or press 2 to quit: ')
        try:
            user_selection = int(user_selection)
        except ValueError:
            print('Wrong entry')
            continue
        if user_selection == 2:
            print('You have exited the application.')
            quit()
        elif user_selection == 1:
            print('PlayStation game genres: ')
            games_genre()
        else: 
            print('Please select 1 or 2: ')
        
        
user_choice()

