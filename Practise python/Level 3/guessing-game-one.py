# https://www.practicepython.org/exercise/2014/04/02/09-guessing-game-one.html
# Exercise 9
# 
# Main
# Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number, then tell them 
# whether they guessed too low, too high, or exactly right. (Hint: remember to use the user input lessons from 
# the very first exercise)
# 
# Extras:
# 1. Keep the game going until the user types “exit”
# 2. Keep track of how many guesses the user has taken, and when the game ends, print this out.
import random

while True:
    tries = 0
    # Generate random number between 1 and 9
    randomNumber = random.randint(1, 9)

    print( 'Write "exit" if you want to quit the game' )
    print( 'New game!' )
    
    # Check if user wants to quit the game
    if playersGuess == 'exit': break


    # Let user keep guessing
    while True:
        playersGuess = input( 'Guess a number between 1 and 9 (including 1 and 9)' )
        
        if playersGuess == 'exit': exit

        tries += 1
        if playersGuess < randomNumber: 
            print( 'You guess too low :(, try again..' )

        if playersGuess > randomNumber: 
            print( 'You guess too high :(, try again..',  ) 

        # Check if player won
        if playersGuess == randomNumber: 
            print( f'You guess correctly, congratulations! It took you {tries}' )
            break
            