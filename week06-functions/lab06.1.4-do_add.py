# Testing out the do_add() function for the student management program.
# Author: Tom Brophy

students = []
def read_modules():
    return []

def do_add(students):
    current_student = {}
    current_student['name'] = input('Enter name: ')
    current_student['modules'] = read_modules()

    students.append(current_student)

do_add(students)

do_add(students)
print(students)
