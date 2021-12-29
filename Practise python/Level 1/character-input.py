# https://www.practicepython.org/exercise/2014/01/29/01-character-input.html
# Exercise 1
#
# Main
# Create a program that asks the user to enter their name and their age. Print out a message
# addressed to them that tells them the year that they will turn 100 years old.
#
# Extras:
# 1. Add on to the previous program by asking the user for another number and printing out that
# many copies of the previous message. (Hint: order of operations exists in Python)
# 2. Print out that many copies of the previous message on separate lines.

# Main #
import datetime

# Get user's name and age
name = input( 'Enter your name: ' )
age = input( 'Enter your age: ' )

# Make sure that age user's provided is numeric
while not( age.isnumeric() ) :
    age = input( 'The year you placed is invalid. Please enter your age: ') 

# Calculate when user will turn 100
now = datetime.datetime.now()
hundredYear = now.year + ( 100 - int(age) )

# Print the result
print( f'Hello {name}, on year {hundredYear} you will turn 100' )

# Extras
repeat = input( 'How many times would you like to repeat this massage?: ')

# Make sure that age user provided is numeric
while not( age.isnumeric() ) :
    repeat = input( 'The number you placed is invalid. Please enter a number: ') 

# Print the result that many times
for i in range( int( repeat ) ) :
    print( f'Hello {name}, on year {hundredYear} you will turn 100' )