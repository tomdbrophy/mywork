# div.py
# Divides one user entered number by another
# Author: Tom Brophy

x = int(input('Enter first number: '))
y = int(input('Enter the number you want to divide by: '))
answer = int(x//y)  #int division
remainder = x%y     #remainder

print('{} divided by {} is {} with remainder {}'.format(x,y,answer,remainder))
