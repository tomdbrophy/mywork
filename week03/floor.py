# floor.py
# Takes in a float and outputs an int rounded down
# Author: Tom Brophy

import math

number_to_floor = float(input('Enter a float number: '))
floored_number = math.floor(number_to_floor)
print(f'{number_to_floor} floored is {floored_number}')
