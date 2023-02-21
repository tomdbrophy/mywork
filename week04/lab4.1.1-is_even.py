# is_even.py
# Tells the user if a number they enter is even or odd
# Author: Tom Brophy

number = int(input('Enter an integer:'))

if (number % 2) == 0:
    print (f'{number} is an even number')
else:
    print (f'{number} is an odd number')
    