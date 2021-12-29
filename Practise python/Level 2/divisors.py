# https://www.practicepython.org/exercise/2014/02/26/04-divisors.html
# Exercise 4
# 
# Main
# Create a program that asks the user for a number and then prints out a list of all the divisors of that number.
# (If you don’t know what a divisor is, it is a number that divides evenly into another number. For example,
# 13 is a divisor of 26 because 26 / 13 has no remainder.)

# Get user's number
usersNumber = int( input( 'Your number: ' ) )

# Find divisors of user's number (+1 because we also want to divide by itself, from from 0 to not devide from 0 )
print( f'Found divisors: {[ num for num in range(1, usersNumber + 1 ) if usersNumber % num == 0  ]}' )