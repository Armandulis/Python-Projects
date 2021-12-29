# https://www.practicepython.org/exercise/2014/02/05/02-odd-or-even.html
# Exercise 2
#
# Main:
# Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the
# user. Hint: how does an even / odd number react differently when divided by 2?
# 
# Extras:
# 1. If the number is a multiple of 4, print out a different message.
# 2. Ask the user for two numbers: one number to check (call it num) and one number to divide by (check).
# If check divides evenly into num, tell that to the user. If not, print a different appropriate message.

# Main #
# Get user's number
number = input( 'Your number: ' )

# Make sure that number user's provided is numeric
while not( number.isnumeric() ) :
    number = input( 'The number you provided is not a number. Please provided a number: ')

if ( int(number) % 2 ) == 0:
    print( f'Your number {number} is even' )
else:
    print( f'Your number {number} is NOT even' )

# Extras #
# Check if user's number is a multiple of 4
if ( int(number) % 4 ) == 0:
    print( f'Your number {number} is a multiple of 4' )
else:
    print( f'Your number {number} is NOT a multiple of 4' )

# Get user's number
number = input( 'Your number: ' )
multiple = input( 'Check if it\'s a multiple of: ' )

# Make sure that number user's provided is numeric
while not( number.isnumeric() ) :
    number = input( 'The number you provided is not a number. Please provided a number: ')
while not( multiple.isnumeric() ) :
    multiple = input( 'The multiple of number you provided is not a number. Please provided a multiple of number: ')

# Check if users number is multiple of user's multiple
if ( int( number ) % int( multiple ) ) == 0:
    print( f'Your number {number} is a multiple of {multiple}' )
else:
    print( f'Your number {number} is NOT a multiple of {multiple}' )