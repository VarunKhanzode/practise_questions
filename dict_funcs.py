
# Unordered (Python 3.7+ maintains insertion order, but conceptually not designed for order)

# Mutable

# Keys are unique

# When to use:

# When you want to map one thing to another (key-value relationships).

# When you need fast lookup based on a key.

# Real-time examples:

# User profile (name, email, age).

# Configuration settings for an app (like API keys, DB connection details).

# Storing word counts in a paragraph.

# dictionary_examples.py

# Dictionary creation
my_dict = {'a': 1, 'b': 2, 'c': 3}

# len() - number of key-value pairs
print(len(my_dict))  # Output: 3

# type() - type of object
print(type(my_dict))  # Output: <class 'dict'>

# str() - string representation
print(str(my_dict))  # Output: {'a': 1, 'b': 2, 'c': 3}

# keys() - returns keys
print(list(my_dict.keys()))  # Output: ['a', 'b', 'c']

# values() - returns values
print(list(my_dict.values()))  # Output: [1, 2, 3]

# items() - returns key-value pairs
print(list(my_dict.items()))  # Output: [('a', 1), ('b', 2), ('c', 3)]

# get() - gets value for a key
print(my_dict.get('b'))  # Output: 2

# get() with default value
print(my_dict.get('d', 'Not Found'))  # Output: Not Found

# update() - update with another dictionary
my_dict.update({'d': 4})
print(my_dict)  # Output: {'a': 1, 'b': 2, 'c': 3, 'd': 4}

# pop() - removes key and returns value
print(my_dict.pop('a'))  # Output: 1
print(my_dict)  # Output: {'b': 2, 'c': 3, 'd': 4}

# popitem() - removes and returns last inserted key-value pair
print(my_dict.popitem())  # Output: ('d', 4)
print(my_dict)  # Output: {'b': 2, 'c': 3}

# clear() - removes all elements
my_dict.clear()
print(my_dict)  # Output: {}

# copy() - shallow copy of dictionary
original = {'x': 10, 'y': 20}
copy_dict = original.copy()
print(copy_dict)  # Output: {'x': 10, 'y': 20}

# fromkeys() - creates dictionary from keys with same value
new_dict = dict.fromkeys(['p', 'q', 'r'], 0)
print(new_dict)  # Output: {'p': 0, 'q': 0, 'r': 0}

data = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
sorted_desc = dict(sorted(data.items(), key=lambda item: item[1], reverse=True))
print(sorted_desc)
# Output: {'d': 4, 'c': 3, 'b': 2, 'a': 1}
