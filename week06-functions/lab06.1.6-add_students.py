# Expands on previous iterations joining together what's done so far.
# Author: Tom Brophy

def display_menu():
    print('What would you like to do?')
    print('\t(a) Add new student')
    print('\t(v) View students')
    print('\t(q) Quit')
    choice = input('Type one letter: a/v/q: ').strip()
    return choice

def do_add(students):
    current_student = {}
    current_student['name'] = input('Enter name: ')
    current_student['modules'] = read_modules()
    students.append(current_student)

def read_modules():
    modules = []
    module_name = input('\tEnter the first module name (blank to quit): ').strip()
    while module_name != '':
        module = {}
        module['name'] = module_name
        module['grade'] = int(input('\t\tEnter grade: '))
        modules.append(module)
        module_name = input('\tEnter the next module name (blank to quit): ').strip()
    return modules

def do_view():
    print('In viewing')

students = []
choice = display_menu()
while choice != 'q':
    if choice == 'a':
        do_add(students)
    elif choice == 'v':
        do_view(students)
    elif choice != 'q':
        print('\n\nPlease select either a, v, or q')
    choice = display_menu()


# Test the function
choice = display_menu()
print(f'You chose: {choice}')
