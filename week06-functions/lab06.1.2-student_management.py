# Defines a function to take in user input from a set menu.
# Author: Tom Brophy

def display_menu():
    print('What would you like to do?')
    print('\t(a) Add new student')
    print('\t(v) View students')
    print('\t(q) Quit')
    choice = input('Type one letter: a/v/q: ').strip()

    return choice

# Test the function
choice = display_menu()
print(f'You chose: {choice}')
