# grade.py
# Reads in a percentage mark, rounds it, and prints out the corresponding grade
# Author: Tom Brophy

percentage = float (input('Enter a percentage: '))

# Alternative solution to using round would be change the numbers in the if statement
# E.g. <39.5 = Fail
rounded = round(percentage)

if rounded < 0 or percentage > 100:
    print('Please enter a number between 0 and 100')
elif rounded < 40:
    print('Fail')
elif rounded < 50:
    print('Pass')
elif rounded < 60:
    print('Merit1')
elif rounded < 70:
    print('Merit2')
else:
    print('Distinction')
    