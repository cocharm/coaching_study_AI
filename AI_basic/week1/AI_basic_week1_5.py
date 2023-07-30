import re
inputs = "cat32dog16cow5"

def find_string(inputs):
    return re.sub("[0-9]", "",inputs)    

string_list = find_string(inputs)
print(string_list)