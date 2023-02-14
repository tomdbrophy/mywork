# normalise.py
# Changes string to lower case and removes leading/trailing spaces
# Author: Tom Brophy

raw_string = input('Please enter a string: ')
normalised_string = raw_string.strip().lower()

length_of_raw_string = len(raw_string)
length_of_normalised = len(normalised_string)

print(f'That string normalised is: {normalised_string}')
print(f'We reduced the input string from {length_of_raw_string} to {length_of_normalised} characters')
