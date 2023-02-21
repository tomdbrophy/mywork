# guess2.py
# User repeatedly guesses number with program giving feedback to aid in future guesses (high/low)
# Author: Tom Brophy

number_to_guess = 30

guess = int(input('Please guess the number: '))
while guess != number_to_guess:
    if guess < number_to_guess:
        print('Too low!')
    else:
        print('Too high')
    guess = int(input('Plesae guess again'))

print('Well done! Yes the number was ', number_to_guess)