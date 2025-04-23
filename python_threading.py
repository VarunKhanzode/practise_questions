# Multithreading in Python involves running multiple threads concurrently within a single process 
# to achieve parallelism and utilize  multiple CPU cores 

import threading

def func1(n):
    for i in range(n):
        print(f"square of {i} is : {i**2}")

def func2(n):
    for i in range(n):
        print(f"cube of {i} is : {i**3}")

t1 = threading.Thread(target=func1, args=(10,))
t2 = threading.Thread(target=func2, args=(10,))

t1.start()
t2.start()
