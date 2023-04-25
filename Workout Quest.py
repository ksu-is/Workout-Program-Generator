import random
import json

with open('player_stats.txt','w') as player_stats:
    json.dump(player,player_stats)

# Initialize the player's stats
player = {'name': '', 'level': 1, 'strength': 10, 'stamina': 10, 'experience': 0}

# List of available exercises
exercises = ['Push-ups', 'Sit-ups', 'Squats', 'Lunges', 'Plank']

# Function to select a random exercise from the list
def select_exercise():
    return random.choice(exercises)

# Function to display the player's stats
def show_stats():
    print(f'Name: {player["name"]}')
    print(f'Level: {player["level"]}')
    print(f'Strength: {player["strength"]}')
    print(f'Stamina: {player["stamina"]}')
    print(f'Experience: {player["experience"]}')

# Function to start the game
def start_game():
    player['name'] = input('Enter your name: ')
    # Loop through the game until the player chooses to quit
    while True:
        # Display the player's stats
        show_stats()

        # Give the player a choice of exercises
        print('\nWhich exercise would you like to do today?')
        for i, exercise in enumerate(exercises):
            print(f'{i + 1}. {exercise}')

        # Get input from the player
        choice = input('> ')

        # Handle the player's choice
        if choice.isdigit() and int(choice) in range(1, len(exercises) + 1):
            exercise = exercises[int(choice) - 1]
            reps = int(input(f'How many reps of {exercise} do you want to do? '))
            print(f'You chose to do {reps} reps of {exercise}!')

            # Calculate the player's results
            if exercise == 'Push-ups':
                experience = reps
                strength = 0.33 * reps
                stamina = 0.1 * reps
            elif exercise == 'Sit-ups':
                experience = reps
                strength = 0.25 * reps
                stamina = 0.1 * reps
            elif exercise == 'Squats':
                experience = reps
                strength = 0.2 * reps
                stamina = 0.1 * reps
            elif exercise == 'Lunges':
                experience = reps
                strength = 0.2 * reps
                stamina = 0.05 * reps
            elif exercise == 'Plank':
                experience = reps
                strength = 0.1 * reps
                stamina = 0.2 * stamina

            # Update the player's stats
            player['experience'] += experience
            player['strength'] += strength
            player['stamina'] += stamina

            if player['experience'] >= 10 * player['level']:
                player['level'] += 1
                player['strength'] += 4
                player['stamina'] += 2
                print(f'Congratulations, you leveled up to level {player["level"]}!')
        elif choice.lower() == 'quit':
            break
        else:
            print('Invalid choice.')

    # Game over
    print(f'Thanks for playing, {player["name"]}!')

# Start the game
start_game()

