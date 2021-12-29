# https://www.practicepython.org/exercise/2014/02/15/03-list-less-than-ten.html
# Exercise 3
# 
# Main
# Take a list, say for example this one: "a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]"
# and write a program that prints out all the elements of the list that are less than 5.
#
# Extras:
# 1. Instead of printing the elements one by one, make a new list that has all the elements less than 5 
# from this list in it and print out this new list.
# 2. Write this in one line of Python.
# 3. Ask the user for a number and return a list that contains only elements from the original list a 
# that are smaller than that number given by the user.

list = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
newList = []
# Loop through numbers in list and print smaller than 5 ones
for num in list:
    if num < 5:
        print( num )
        newList.append( num )

# Extras
# Print new list
print( f'New list: {newList}' )

# Same as lines 14-19 just in one line
print( f'One line {[ num for num in list if num < 5 ]}' )

# With users input
# Get user's number
number = input( 'Your number: ' )

# Make sure that number user's provided is numeric
while not( number.isnumeric() ) :
    number = input( 'The number you provided is not a number. Please provided a number: ')
    
# Print numbers that are smallers than users number
print( f'One line {[ num for num in list if num < int( number ) ]}' )