# INF322 Python

# Josh Lewis

# Week 2 – Guess the Magician's Card

import random

def game():
    cardSuit = random.randint(1, 4)
    cardValue = random.randint(1, 14)
    
    # SUIT GUESSING SECTION
    print('Guess the card suit. 1 (Spades), 2 (Hearts) 3 (Diamonds), 4 (Clubs)')

    # Allow four guesses
    for suitGuesses in range(1, 5):
        print('Take a guess.')
        suitGuess = int(input())

        if suitGuess < cardSuit:
            print('Guess a higher suit.')
        elif suitGuess > cardSuit:
            print('Guess a lower suit.')
        else:
            break    # This condition is the correct suit!

    if suitGuess == cardSuit:
        print('Good job! You guessed the correct suit in ' + str(suitGuesses)
              + (' guesses' if (suitGuesses > 1) else ' guess') + '!')
    else:
        print('Nope. The correct suit was ' +
              ('Spades' if (cardSuit == 1) else 'Hearts' if (cardSuit == 2) else
              'Diamonds' if (cardSuit == 3) else 'Clubs' if (cardSuit == 4) else str(None)))

    # VALUE GUESSING SECTION
    print('Guess the card value. 1 to 10, or 11 (Jack), 12 (Queen), 13 (King), 14 (Ace)')

    # Allow six guesses
    for valueGuesses in range(1, 6):
        print('Take a guess.')
        valueGuess = int(input())

        if valueGuess < cardValue:
            print('Guess a higher card.')
        elif valueGuess > cardValue:
            print('Guess a lower card.')
        else:
            break    # This condition is the correct suit!

    if valueGuess == cardValue:
        print('Good job! You guessed the correct card in ' + str(valueGuesses)
              + (' guesses' if (valueGuesses > 1) else ' guess') + '!')
    else:
        if cardValue >= 11:
            if cardValue == 11:
                   faceCard = 'Jack'
            elif cardValue == 12:
                   faceCard = 'Queen'
            elif cardValue == 13:
                   faceCard = 'King'
            else:
                   faceCard = 'Ace'
            print('Nope. The correct card was ' + faceCard)
        else:
            print('Nope. The correct card was ' + str(cardValue) + '.')

    #FINAL ANSWER
    if cardValue >= 11:
        print('The magician\'s secret card was the ' + faceCard + ' of ' +
              ('Spades' if (cardSuit == 1) else 'Hearts' if (cardSuit == 2) else
              'Diamonds' if (cardSuit == 3) else 'Clubs' if (cardSuit == 4) else None) + '!')
    else:
        print('The magician\'s secret card was the ' + str(cardValue) + ' of ' +
              ('Spades' if (cardSuit == 1) else 'Hearts' if (cardSuit == 2) else
              'Diamonds' if (cardSuit == 3) else 'Clubs' if (cardSuit == 4) else None) + '!')

while True:
    answer = input('Would you like to play Guess the Magician\'s Card again? (Y/N): ')
    if answer == 'Y' or answer == 'y':
        game()
        continue
    elif answer == 'N' or answer == 'n':
        print('Thanks for playing!')
        break
    else:
        print("Invalid entry. Please type Y or N.")
