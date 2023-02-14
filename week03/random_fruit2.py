# random_fruit.py
# Prints out a random fruit from a list
# Author: Tom Brophy

import random

fruits = ('apple', 'orange', 'banana', 'pear')

index = random.randint(0,len(fruits)-1)

fruit = fruits[index]
print('A random fruit: {}'.format(fruit))
