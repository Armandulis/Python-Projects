# https://www.practicepython.org/exercise/2014/03/12/06-string-lists.html
# Exercise 6
# Ask the user for a string and print out whether this string is a palindrome or not.
# (A palindrome is a string that reads the same forwards and backwards.)

# Get user's word
usersWord = input( 'Your word: ' ).lower()

# Use 'reverse' function to reverse word
temp = ''
for char in reversed( usersWord ):
    temp += char

if usersWord == temp: print( f' Your word "{ usersWord }" is palindrome!')
else: print( f' Your word "{ usersWord }" is NOT palindrome!')

# Or use [::-1], string[ 0:5 ] - keys to get characters at that location in the array
if usersWord == usersWord[::-1]: print( f' Your word "{ usersWord }" is palindrome!')
else: print( f' Your word "{ usersWord }" is NOT palindrome!')
