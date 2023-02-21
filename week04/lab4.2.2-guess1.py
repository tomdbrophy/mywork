# guess.py
# Prompts user to repeatedly guess a number until user guesses correctly.
# Author: Tom Brophy

number_to_guess = 30

guess = int(input('Please guess the number: '))
while guess != number_to_guess:
    print('Wrong')
    guess = int(input('Plesae guess again: '))

print('Well done! Yes the number was ', number_to_guess)
