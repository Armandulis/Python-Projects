# https://www.practicepython.org/exercise/2014/03/05/05-list-overlap.html
# Exercise 5
# 
# Main
# Take two lists, say for example these two:
#   a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#   b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# and write a program that returns a list that contains only the elements that are common between the
# lists (without duplicates). Make sure your program works on two lists of different sizes.
# 
# Extras:
# 1. Randomly generate two lists to test this
# 2. Write this in one line of Python (don’t worry if you can’t figure this out at this point - we’ll get to it soon)

# Main
import random
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
common = []

# Loop through bothg list and compare numbers
for first in a:
    for second in b:
        if second == first:
            common.append( first )

print( f'Common numbers {common}')

# Extras

# Generate random arrays
randomA = random.sample( range( 1, 100 ), 50 )
randomB = random.sample( range( 1, 100 ), 50 )

# Lines 22-27 in one line
print( f'One line common numbers {[ commonFirst for commonFirst in randomA for commonSecond in randomB if commonFirst == commonSecond ]}' )

# Found this one on the internet, looks easy enough
print( set(a) & set(b) ) # the & is for intersection, which will take the common between the two