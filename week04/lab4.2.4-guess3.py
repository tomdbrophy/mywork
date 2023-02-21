# guess3.py
# User repeatedly guesses randomly generatednumber.
# Program gives feedback to aid in future guesses (high/low).
# Author: Tom Brophy

import random


number_to_guess = random.randint(0,100)

guess = int(input('Please guess the number between 0 and 100: '))
while guess != number_to_guess:
    if guess < number_to_guess:
        print('Too low!')
    else:
        print('Too high')
    guess = int(input('Plesae guess again: '))

print('Well done! Yes the number was ', number_to_guess)