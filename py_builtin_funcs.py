# builtin_functions_examples.py

# 1. len() - Get the length of a string, list, or other iterable
print("Length of 'Hello':", len("Hello"))

# 2. type() - Get the type of an object
print("Type of 42:", type(42))

# 3. int(), float(), str() - Type casting
print("Convert '10' to int:", int("10"))
print("Convert 5 to string:", str(5))

# 4. range() - Generate a sequence of numbers
for i in range(3):
    print("Range example:", i)

# 5. enumerate() - Get index and value in a loop
fruits = ['apple', 'banana', 'cherry']
for idx, fruit in enumerate(fruits):
    print(f"Fruit {idx} is {fruit}")

# 6. zip() - Combine two or more iterables
names = ["Alice", "Bob"]
scores = [85, 90]
for name, score in zip(names, scores):
    print(f"{name} scored {score}")

# 7. map() - Apply a function to every item in an iterable
nums = [1, 2, 3]
squared = list(map(lambda x: x ** 2, nums))
print("Squared numbers:", squared)

# 8. filter() - Filter items based on a condition
even_nums = list(filter(lambda x: x % 2 == 0, nums))
print("Even numbers:", even_nums)

# 9. sorted(), reversed()
unsorted = [3, 1, 4, 1]
print("Sorted list:", sorted(unsorted))
print("Reversed list:", list(reversed(unsorted)))

# 10. sum(), max(), min()
print("Sum:", sum(nums))
print("Max:", max(nums))
print("Min:", min(nums))

# 11. any(), all()
bools = [True, False, True]
print("Any true?:", any(bools))
print("All true?:", all(bools))

# 12. isinstance()
print("Is 5 an int?:", isinstance(5, int))

# 13. input() - Get user input (commented to avoid blocking)
# name = input("Enter your name: ")
# print("Hello", name)

# 14. open() - File operations
with open("sample.txt", "w") as f:
    f.write("Hello file!")
with open("sample.txt", "r") as f:
    print("File content:", f.read())

# 15. eval() - Evaluate string as Python expression (use carefully!)
expr = "3 * (2 + 1)"
print("Eval result:", eval(expr))

# 16. dir(), help()
print("Attributes of a list object:", dir([]))
# Uncomment the below line to view documentation (only in interactive shell)
# help(len)

# 17. hasattr(), getattr(), setattr()
class Demo:
    x = 10

demo = Demo()
print("Has attribute x?", hasattr(demo, 'x'))
print("Value of x:", getattr(demo, 'x'))
setattr(demo, 'y', 20)
print("New attribute y:", demo.y)

# 18. chr(), ord()
print("Char for 65:", chr(65))
print("ASCII of 'A':", ord('A'))


# standard_library_examples.py

# --- 1. os: Operating system interaction ---
import os

print("Current working directory:", os.getcwd())
print("List of files in current directory:", os.listdir('.'))

# --- 2. sys: System-specific parameters and functions ---
import sys

print("Python version:", sys.version)
print("Command line arguments:", sys.argv)

# --- 3. datetime: Working with dates and times ---
from datetime import datetime, timedelta

now = datetime.now()
print("Current time:", now)
print("Yesterday was:", now - timedelta(days=1))

# --- 4. time: Sleep or measure performance ---
import time

start = time.time()
time.sleep(1)  # Sleep for 1 second
print("Elapsed time:", time.time() - start)

# --- 5. random: Generate random numbers ---
import random

print("Random integer between 1 and 10:", random.randint(1, 10))
print("Random choice from list:", random.choice(['a', 'b', 'c']))

# --- 6. json: Encode/decode JSON data ---
import json

data = {'name': 'Alice', 'age': 25}
json_str = json.dumps(data)
print("JSON string:", json_str)
parsed = json.loads(json_str)
print("Parsed JSON:", parsed)

# --- 7. math: Math functions ---
import math

print("Square root of 16:", math.sqrt(16))
print("PI value:", math.pi)

# --- 8. collections: High-performance container datatypes ---
from collections import Counter, defaultdict, namedtuple

# Counter
counter = Counter('banana')
print("Counter example:", counter)

# defaultdict
dd = defaultdict(int)
dd['key'] += 1
print("Defaultdict example:", dd)

# namedtuple
Point = namedtuple('Point', 'x y')
pt = Point(1, 2)
print("Namedtuple:", pt, pt.x, pt.y)

# --- 9. itertools: Advanced iteration tools ---
import itertools

print("Product:", list(itertools.product([1, 2], ['a', 'b'])))
print("Permutations of [1, 2, 3]:", list(itertools.permutations([1, 2, 3])))

# --- 10. functools: Higher-order functions ---
from functools import reduce

nums = [1, 2, 3, 4]
sum_nums = reduce(lambda x, y: x + y, nums)
print("Sum using reduce:", sum_nums)

# --- 11. pathlib: Modern file path handling ---
from pathlib import Path

path = Path(".")
print("Path exists?", path.exists())
print("Files in path:", list(path.glob("*.py")))

# --- 12. subprocess: Run external commands ---
import subprocess

result = subprocess.run(["echo", "Hello from subprocess"], capture_output=True, text=True)
print("Subprocess output:", result.stdout.strip())

# --- 13. re: Regular expressions ---
import re

pattern = r'\d+'
matches = re.findall(pattern, '123 abc 456')
print("Regex matches:", matches)

# --- 14. logging: Logging messages ---
import logging

logging.basicConfig(level=logging.INFO)
logging.info("This is an info message")
logging.warning("This is a warning message")

# --- 15. threading: Run tasks in parallel ---
import threading

def print_numbers():
    for i in range(5):
        print("Number:", i)

thread = threading.Thread(target=print_numbers)
thread.start()
thread.join()
