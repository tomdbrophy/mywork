# Allows user to enter student data and stores it in a callable dict format.
# Author: Tom Brophy

student_name = str(input('Enter student name: '))

module_title = {str(input('Enter module name: '))}
module_name = {'course_name':module_title}

module_names = []

while module_title != '':
    module_names.append(module_name)
    module_title = str(input('Enter module name: '))
    module_name = {'course_name':module_title}

student = {
    'name': student_name,
    'modules': module_names
}

print(student['name'])
print(student['modules'])