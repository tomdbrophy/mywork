# Reads a dict object from a file.
# Author: Tom Brophy

import json
FILENAME = 'testdict.json'

def read_dict():
    with open(FILENAME) as f:
        return json.load(f)

somedict = read_dict()
print(somedict)