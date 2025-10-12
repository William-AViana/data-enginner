import re

string = "  My name is William and i am learning data enginner."
#print(string[5])
#print(string[10:20])
#print(len(string))

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

# working with lists

numbers = [1, 2, 3, 4, 5]
print(numbers[2])

print(numbers[1:4])
print(numbers[:2])
print(numbers[3:])
numbers[4]= 6
print(numbers)

numbers.append(5) # insert an element to end of list
print(numbers)

numbers.insert(2, 7) # insert an element ata specific index
print(numbers)

numbers.remove(7)
print(numbers)

element_popped = numbers.pop(4)
print(element_popped)

del numbers[4]
print(numbers)

index_of_element = numbers.index(1)
print(index_of_element)

numbers.append(5)
numbers.append(3)
numbers.append(5)
count = numbers.count(5)
print(count)

numbers.reverse()
print(numbers)

numbers.sort()
print(numbers)

# list Comprehension
squared = [num ** 2 for num in numbers if num % 2 == 0]
print(squared)

even = [num for num in range(1, 8) if num % 2 == 0]
print(even)

# Built-in functions and methods
length = len(numbers)
print(length)

minimum = min(numbers)
maximum = max(numbers)
print(minimum, maximum)

total = sum(numbers)
print(total)

new_list_sorted = sorted(numbers) # not modify original list
print(new_list_sorted)

new_list_sorted.clear()
print(new_list_sorted)

new_copy_of_list = numbers.copy()
new_copy_of_list.reverse()
print(new_copy_of_list)

nested_list = [numbers, new_copy_of_list]
print(nested_list[0])

# Sets
my_set = {1, 2, 3}
#print(my_set)

another_set = set([4, 5, 6, 7])
#print(another_set)

unique_set = {1, 2, 3, 3, 4, 5, 5, 6, 6, 7}
print(unique_set)

# Basic operator
set_a = {1, 2, 3}
set_b = {3, 4, 5}

# Union
union_resul = set_a | set_b # or use set_a,union(set_b)
print(union_resul)

# Intersection
intersection_result = set_a & set_b # or use set_a.intersection(set_b)
print(intersection_result)

# Difference
difference_result = set_a - set_b # or use set_a.difference(set_b)
print(difference_result)

# Symmetric Difference
symmetric_result = set_a ^ set_b
print(symmetric_result)

# Sets methods
my_set.add(4)
print(my_set)

my_set.remove(2)
print(my_set)

my_set.discard(3)
print(my_set)

my_set.clear()
print(my_set)

my_set =  {1, 2, 3, 4}
print(2 in my_set)
print(5 in my_set)

print(len(my_set))
