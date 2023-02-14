# extras3.2.py
# Extra question in lab 3.2
# Author: Tom Brophy

import math

dollar_amount = float(input('Please enter an amount: '))
absolute_dollars = abs(dollar_amount)
#print(absolute_dollars)
cents = int(absolute_dollars*100)
print(f'The amount in cent is: {cents}')