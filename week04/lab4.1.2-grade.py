# grade.py
# Reads in a percentage nmark and prints out the corresponding grade
# Author: Tom Brophy

percentage = float (input('Enter a percentage: '))

if percentage < 0 or percentage > 100:
    print('Please enter a number between 0 and 100')
elif percentage < 40:
    print('Fail')
elif percentage < 50:
    print('Pass')
elif percentage < 60:
    print('Merit1')
elif percentage < 70:
    print('Merit2')
else:
    print('Distinction')
    