# topthree.py
# Generates 10 random numbers and selects the top three
# Author: Tom Brophy

import random

how_many = 10
top_how_many = 3
range_from = 0
range_to = 100

numbers = []

for i in range(0,how_many):
    numbers.append(random.randint(range_from, range_to))
print(f'{how_many} random numbers\t {numbers}')

top_ones = numbers.copy()

top_ones.sort(reverse=True)
print(f'The top {top_how_many} are \t\t {top_ones[0:top_how_many]}')
