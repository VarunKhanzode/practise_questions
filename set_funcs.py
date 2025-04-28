# set_examples.py

# Set creation
my_set = {1, 2, 3, 4, 5}

# len() - number of elements
print(len(my_set))  # Output: 5

# type() - type of object
print(type(my_set))  # Output: <class 'set'>

# max() - maximum element
print(max(my_set))  # Output: 5

# min() - minimum element
print(min(my_set))  # Output: 1

# sum() - sum of elements
print(sum(my_set))  # Output: 15

# sorted() - sorted list from set
print(sorted(my_set))  # Output: [1, 2, 3, 4, 5]

# set() - create set
print(set([1, 2, 2, 3]))  # Output: {1, 2, 3}

# add() - adds an element
my_set.add(6)
print(my_set)  # Output: {1, 2, 3, 4, 5, 6}

# update() - updates set with multiple elements
my_set.update([7, 8])
print(my_set)  # Output: {1, 2, 3, 4, 5, 6, 7, 8}

# remove() - removes an element (raises KeyError if not found)
my_set.remove(8)
print(my_set)  # Output: {1, 2, 3, 4, 5, 6, 7}

# discard() - removes element if present (no error if not found)
my_set.discard(10)  # No error

# pop() - removes and returns an arbitrary element
print(my_set.pop())  # Output: (random element)

# clear() - removes all elements
my_set.clear()
print(my_set)  # Output: set()

# union() - returns union of sets
set1 = {1, 2}
set2 = {2, 3}
print(set1.union(set2))  # Output: {1, 2, 3}

# intersection() - common elements
print(set1.intersection(set2))  # Output: {2}

# difference() - elements in set1 but not in set2
print(set1.difference(set2))  # Output: {1}

# symmetric_difference() - elements in either set1 or set2 but not both
print(set1.symmetric_difference(set2))  # Output: {1, 3}

# issubset() - whether set1 is subset of set2
print({1, 2}.issubset({1, 2, 3}))  # Output: True

# issuperset() - whether set1 is superset of set2
print({1, 2, 3}.issuperset({1, 2}))  # Output: True

# isdisjoint() - returns True if sets have no elements in common
print({1, 2}.isdisjoint({3, 4}))  # Output: True
