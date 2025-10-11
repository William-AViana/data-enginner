import re

string = "  My name is William and i am learning data enginner."

new_string = string.split(' ')
print(new_string)

string_join = string.join(new_string)
print(string_join)

string_strip = string.strip()
print(string_strip)

string_replace = string.replace(' ', ', ')
print(string_replace)

