# INF322 Python
# Josh Lewis
# Midterm Project: GAME – Rock, Paper, Scissors, Lizard, Spock

import random

print("You are playing Rock, Paper, Scissors, Lizard, Spock.")

# Asks user to type a choice from the list provided
def getUserInput():
    while True:
        playerInput = input("Make a choice: {} ".format(list(beats.keys())))
        if playerInput in beats: # If user choice matches acceptable key or value in dictionary
            return playerInput # Make function return value
        print("Invalid choice.")

# Dictionary contains fail conditions as keys, and sub-dictionaries of winning values
beats = {'rock': {'paper', 'spock'},
         'paper': {'scissors', 'lizard'},
         'scissors': {'rock', 'spock'},
         'lizard': {'scissors', 'rock'},
         'spock': {'paper', 'lizard'}}

# Dictionary is used to format game output to describe how player beats computer or vice versa
verbs = {'rock': 'smashes',
        'paper': 'discredits',
        'scissors': 'slice',
        'lizard': 'eats',
        'spock': 'vaporizes'}

# Scoring mechanism for game
def calculator():
    computerChoice = random.choice(list(beats.keys())) # Chooses random key from beats dictionary
    playerInput = getUserInput() # Retrieves value entered by user and assigns to playerInput
    playerWinsVerb = verbs[playerInput] # Controls verb used to describe player's win condition 
    computerWinsVerb = verbs[computerChoice] # Controls verb used to describe computer's win condition

    # If/else statement to control game output, formatted based on win conditions
    if playerInput in beats[computerChoice]:
        print("{} {} {}, you win!".format(playerInput, playerWinsVerb, computerChoice))
    elif computerChoice in beats[playerInput]:
        print("{} {} {}, computer wins!".format(computerChoice, computerWinsVerb, playerInput))
    else:
        print("Tie.")

# Asks user if they'd like to play again
again = 'yes'
while again != 'no':
    calculator()
    again = input("Would you like to play again? ")
print("Thank you for playing.")
