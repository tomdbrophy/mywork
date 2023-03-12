# Testing out the read_modules() function for the student management program.
# Author: Tom Brophy

students = []
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

def do_add(students):
    current_student = {}
    current_student['name'] = input('Enter name: ')
    current_student['modules'] = read_modules()

    students.append(current_student)

do_add(students)

do_add(students)
print(students)
