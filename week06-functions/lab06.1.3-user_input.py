# Defines a function to take in user input from a set menu.
# This expands on previous iteration to react to user input.
# Author: Tom Brophy

def display_menu():
    print('What would you like to do?')
    print('\t(a) Add new student')
    print('\t(v) View students')
    print('\t(q) Quit')
    choice = input('Type one letter: a/v/q: ').strip()
    return choice

def do_add():
    print('In adding')
def do_view():
    print('In viewing')

choice = display_menu()

while choice != 'q':
    if choice == 'a':
        do_add()
    elif choice == 'v':
        do_view()
    elif choice != 'q':
        print('\n\nPlease select either a, v, or q')
    choice = display_menu()


# Test the function
choice = display_menu()
print(f'You chose: {choice}')
