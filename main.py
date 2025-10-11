import re

string = "  My name is William and i am learning data enginner."
print(string[5])
print(string[10:20])
print(len(string))

new_string = string.split(' ')
print(new_string)

string_join = string.join(new_string)
print(string_join)

string_strip = string.strip()
print(string_strip)

string_replace = string.replace(' ', ', ')
print(string_replace)


# Regex
print(re.split(r'\W+', 'Words, words, words.'))

print(re.split(r'(\W+)', 'Words, words, words.'))

print(re.split(r'\W+', 'Words, words, words.', 1))

print(re.split('[a-f]+', '0a3B9', flags=re.IGNORECASE))

print(re.findall(r'\bf[a-z]*', 'which foot or hand fell fastest'))

