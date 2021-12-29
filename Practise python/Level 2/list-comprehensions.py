# https://www.practicepython.org/exercise/2014/03/19/07-list-comprehensions.html
# Exercise 7 
# 
# Let’s say I give you a list saved in a variable: a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]. Write one line of Python
# that takes this list a and makes a new list that has only the even elements of this list in it.

a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# One line
print( f'Even numbers list one line: {[ number for number in a if number % 2 == 0 ]}' )

# Loop through numbers and find numbers that aree even
evenNumbers = []
for number in a:
    if number % 2 == 0:
        evenNumbers.append(number)

print( f'Even numbers list: {evenNumbers}' )