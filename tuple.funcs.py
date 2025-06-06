# Ordered

# Immutable (cannot change elements once created)
# You cannot change an element.
# You cannot add a new element.
# You cannot remove an element.

# Allows duplicates

# When to use:

# When you need a fixed, constant set of values.

# When you want to use them as keys in dictionaries (because tuples are hashable).

# Real-time examples:

# Geographical coordinates (latitude, longitude) – they don’t change.

# Database records that are fetched as read-only.


# tuple_examples.py

# Tuple creation
my_tuple = (1, 2, 3, 4, 5)

# len() - number of items
print(len(my_tuple))  # Output: 5

# type() - type of object
print(type(my_tuple))  # Output: <class 'tuple'>

# max() - maximum element
print(max(my_tuple))  # Output: 5

# min() - minimum element
print(min(my_tuple))  # Output: 1

# sum() - sum of elements
print(sum(my_tuple))  # Output: 15

# sorted() - returns sorted list (NOT a tuple)
print(sorted(my_tuple))  # Output: [1, 2, 3, 4, 5]

# count() - number of occurrences of a value
print(my_tuple.count(3))  # Output: 1

# index() - index of first occurrence
print(my_tuple.index(4))  # Output: 3

# tuple() - create a tuple
print(tuple([6, 7, 8]))  # Output: (6, 7, 8)

# slicing
print(my_tuple[1:4])  # Output: (2, 3, 4)

# concatenation
print(my_tuple + (6, 7))  # Output: (1, 2, 3, 4, 5, 6, 7)

# repetition
print(my_tuple * 2)  # Output: (1, 2, 3, 4, 5, 1, 2, 3, 4, 5)

# membership test
print(3 in my_tuple)  # Output: True
