# list_examples.py

# List creation
my_list = [1, 2, 3, 4, 5]

# len() - returns number of items in list
print(len(my_list))  # Output: 5

# type() - returns the type of object
print(type(my_list))  # Output: <class 'list'>

# max() - returns maximum element
print(max(my_list))  # Output: 5

# min() - returns minimum element
print(min(my_list))  # Output: 1

# sum() - returns sum of elements
print(sum(my_list))  # Output: 15

# sorted() - returns a new sorted list
print(sorted(my_list, reverse=True))  # Output: [5, 4, 3, 2, 1]

# list() - creates a list
print(list('abc'))  # Output: ['a', 'b', 'c']

# any() - returns True if any element is True
print(any([0, False, 5]))  # Output: True

# all() - returns True if all elements are True
print(all([1, True, 5]))  # Output: True

# enumerate() - returns an enumerate object
for index, value in enumerate(my_list):
    print(index, value)
# Output:
# 0 1
# 1 2
# 2 3
# 3 4
# 4 5

# zip() - pairs elements from multiple lists
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
print(list(zip(list1, list2)))
# Output: [(1, 'a'), (2, 'b'), (3, 'c')]

# map() - apply function to every element
print(list(map(lambda x: x * 2, my_list)))
# Output: [2, 4, 6, 8, 10]

# filter() - filter elements
print(list(filter(lambda x: x % 2 == 0, my_list)))
# Output: [2, 4]

# ---------- List Methods ----------

# append() - adds element to end
my_list.append(6)
print(my_list)  # Output: [1, 2, 3, 4, 5, 6]

# extend() - extends list by appending elements from another list
my_list.extend([7, 8])
print(my_list)  # Output: [1, 2, 3, 4, 5, 6, 7, 8]

# insert() - inserts element at given position
my_list.insert(0, 0)
print(my_list)  # Output: [0, 1, 2, 3, 4, 5, 6, 7, 8]

# remove() - removes first occurrence of value
my_list.remove(5)
print(my_list)  # Output: [0, 1, 2, 3, 4, 6, 7, 8]

# pop() - removes element at given position (or last if none specified)
popped_element = my_list.pop()
print(popped_element)  # Output: 8
print(my_list)  # Output: [0, 1, 2, 3, 4, 6, 7]

# index() - returns index of first occurrence
print(my_list.index(4))  # Output: 4

# count() - returns number of occurrences
print(my_list.count(2))  # Output: 1

# reverse() - reverses list in place
my_list.reverse()
print(my_list)  # Output: [7, 6, 4, 3, 2, 1, 0]

# sort() - sorts the list in place
my_list.sort()
print(my_list)  # Output: [0, 1, 2, 3, 4, 6, 7]

# copy() - returns shallow copy
copied_list = my_list.copy()
print(copied_list)  # Output: [0, 1, 2, 3, 4, 6, 7]

# clear() - removes all elements
my_list.clear()
print(my_list)  # Output: []
