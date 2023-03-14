# Reads a .txt file and increases the count number each time it is run.
# Author: Tom Brophy

FILENAME = 'count.txt'
def read_number():
    try:
        with open(FILENAME) as f:
            number = int(f.read())
            return number
    except IOError:
        return 0

num = read_number()
print(f'count at beginning is: {num}')

def write_number(number):
    with open(FILENAME, 'wt') as f:
        f.write(str(number))

num+=1

print(f'This program has been run {num} times.')

write_number(num)