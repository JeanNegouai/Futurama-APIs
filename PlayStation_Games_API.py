import requests

# Fetch data from the API
response = requests.get("https://api.sampleapis.com/playstation/games")

# Convert JSON data to Python list of dictionaries
games = response.json()

# Create a set to store unique developers
original_set = set()

# Create a dictionary to store developers and their corresponding games.
developer_games = {}

# Prompt user for a developer 
print('List of Playstation developers: ')

# Iterate over each 
for game in games: 
    # Use 'get' to access the genre list and retrieve values associated with 'genre' in the dictionary
    developers = game.get('developers', [])
    game_name = game.get('name') # retrieves all of the games name 

    # Check if the genres list is empty, if not skip the game 
    if len(games) == 0:
         continue

    # Add each developers to the set 
    for developer in developers:
        developer_lower = developer.lower()
        original_set.add(developer_lower)
        if developer_lower not in developer_games: 
            developer_games[developer_lower] = []
        developer_games[developer_lower].append(game_name)

# Print unique developers 
for developer in original_set:
     print(developer)


user_developer = input('Enter a developer to see their game contribution(s): ').strip().lower()

# Show games for the entered developer
if user_developer in developer_games:
      print(f'Games from this developer {user_developer}, which contributed to {len(developer_games[user_developer])} game(s): ')
      for game in developer_games[user_developer]:
            print(f'- {game}')
else: 
    print(f'No games were found in {user_developer}.')
    






