# Creates a queue of random numbers and then shortens that list 
# Author: Tom Brophy

import random
queue = []
number_of_numbers = 10
range_to = 100

for n in range(0,number_of_numbers):
    queue.append(random.randint(0,range_to))

print(f'queue is {queue}')

while len(queue) != 0:
    current_number = queue.pop(0)
    print(f'Current number is {current_number} and the queue is {queue}')

print('The queue is now empty')