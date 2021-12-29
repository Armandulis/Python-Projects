# https://www.practicepython.org/exercise/2014/03/26/08-rock-paper-scissors.html
# Exercise 8
# 
# Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input), compare them, print out
# a message of congratulations to the winner, and ask if the players want to start a new game)
# 
# Remember the rules:
# 1. Rock beats scissors
# 2. Scissors beats paper
# 3. Paper beats rock
import getpass

choises = {'1': 'Rock', '2': 'Sissors', '3': 'Paper'}
firstPlayerWins = 'First player wins!'
secondPlayerWins = 'Second player wins!'


print( 'type q to quit' )

# Loop game to continue playing
while True:
    print( f'Type 1 for {choises["1"]} \nType 2 for {choises["2"]} \nType 3 for {choises["3"]}')

    # Use get pass to that users wouldn't see what each other typed
    firstPLayer = getpass.getpass( 'PLayer 1 choice: ' )
    # Check if user wants to quit the game
    if firstPLayer == 'q': break

    secondPlayer = getpass.getpass( 'PLayer 2 choice: ' )
    if secondPlayer == 'q': break
    
    # Check if inputs are the same, then it's a draw
    if firstPLayer == secondPlayer :
        print( 'It\'s a draw!' )

    #Check who's the winner
    if firstPLayer == '1' and secondPlayer == '2' or firstPLayer == '2' and secondPlayer == '3' or firstPLayer == '3' and secondPlayer == '1':
        print( firstPlayerWins )
    else:
        print( secondPlayerWins )
