
# A class is a collection of objects. Classes are blueprints for creating objects. 
# A class defines a set of attributes and methods that the created objects (instances) can have.

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Abstract Class
# An abstract class is a class that cannot be instantiated directly. 
# It is meant to be inherited by other classes, and it defines a common interface or contract that all its subclasses must follow.
# Let’s say you’re building an e-commerce platform. You want to support multiple payment methods: credit card, PayPal, etc.

# Instead of hardcoding the logic, you define an abstract class:
from abc import ABC, abstractmethod
class PaymentGateway(ABC):
    @abstractmethod
    def authenticate(self):
        pass

    @abstractmethod
    def pay(self, amount):
        pass
# Then implement it differently for each provider:
class CreditCardPayment(PaymentGateway):
    def authenticate(self):
        print("Authenticating credit card...")

    def pay(self, amount):
        print(f"Paid {amount} using Credit Card.")

class PayPalPayment(PaymentGateway):
    def authenticate(self):
        print("Redirecting to PayPal...")

    def pay(self, amount):
        print(f"Paid {amount} using PayPal.")

# ✅ Why it's useful:
# Enforces a common structure across all payment types.

# Makes your code extensible — add CryptoPayment without modifying existing code.

# Works well with polymorphism:
def process_payment(gateway: PaymentGateway, amount):
    gateway.authenticate()
    gateway.pay(amount)

process_payment(CreditCardPayment(), 1000)
process_payment(PayPalPayment(), 500)

# --------------------------------------------------------------------------------------------------------------------------------------------------------
#  Encapsulation
#  Concept:
#  Hiding internal object details and exposing only what’s necessary.
# Achieved using private variables and getters/setters.

class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # private attribute

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance

acc = BankAccount(1000)
acc.deposit(500)
print(acc.get_balance())  # 1500

# Use Case:
# Securing sensitive data like passwords, balance, or tokens from unauthorized access.
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Inheritance
# Concept:
# Allows a class to inherit attributes and methods from another class.

class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def start(self):
        print("Starting vehicle...")

class Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model

    def honk(self):
        print("Beep!")

car = Car("Honda", "Civic")
car.start()
car.honk()

# Use Case:
# Code reuse: build specialized classes from generic ones (e.g., Employee → Manager, Developer).
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Polymorphism
#  Concept:
# Allows different classes to be treated as instances of the same class through a common interface.

class Shape:
    def draw(self):
        raise NotImplementedError("Subclasses should implement this!")

class Circle:
    def draw(self):
        return "Drawing a circle"

class Rectangle:
    def draw(self):
        return "Drawing a rectangle"

class Triangle:
    def draw(self):
        return "Drawing a triangle"

# Generic function that uses polymorphism
def draw_shape(shape: Shape):
    print(shape.draw())

draw_shape(Circle())
draw_shape(Rectangle())
draw_shape(Triangle())
# ✅ Use Case:
# Write generic functions that can work with different object types (like a shape drawer that works on Circle, Rectangle, etc.)
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Method Overriding
# ➤ Concept:
# Subclass provides specific implementation of a method already defined in the parent class.

class Parent:
    def greet(self):
        print("Hello from Parent")

class Child(Parent):
    def greet(self):
        print("Hello from Child")

Child().greet()
# ✅ Use Case:
# Specializing behavior in subclasses like customizing API responses in a subclassed view.
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Class vs Instance Attributes
class Student:
    school = "ABC School"  # Class attribute

    def __init__(self, name):
        self.name = name  # Instance attribute

s1 = Student("Alice")
s2 = Student("Bob")

Student.school = "XYZ School"
print(s1.school)  # XYZ School
# ✅ Use Case:
# Use class attributes for shared values (like DB connection) and instance attributes for object-specific data.
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Static Methods and Class Methods
# ➤ Static Method:
# Doesn’t access instance or class data.
class Utility:
    @staticmethod
    def add(x, y):
        return x + y

print(Utility.add(5, 3))

# ➤ Class Method:
# Accesses class data.
class Dog:
    count = 0

    def __init__(self):
        Dog.count += 1

    @classmethod
    def total_dogs(cls):
        return cls.count

Dog()
Dog()
print(Dog.total_dogs())  # 2
# ✅ Use Case:
# Use static methods for utility functions.

# Use class methods as alternative constructors or to manipulate class state.
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Dunder (Magic) Methods
# ➤ Concept:
# Special methods with __ like __init__, __str__, __len__, etc. 
# Dunder methods, or magic methods, are special methods in Python that start and end with double underscores (like __init__, __str__, __add__).
# We use them to define how objects behave with built-in operations like printing, adding, or comparing. This is called operator overloading."

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f"({self.x}, {self.y})"

p1 = Point(1, 2)
p2 = Point(3, 4)
print(p1 + p2)  # Output: (4, 6)
# ✅ Use Case:
# Customize object behavior (like adding, printing, comparing).

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Property Decorators (Getters/Setters)
class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if value < 0:
            raise ValueError("Negative radius not allowed")
        self._radius = value

c = Circle(5)
c.radius = 10
print(c.radius)
# ✅ Use Case:
# Data validation and encapsulation without changing the external API.
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Object Cloning (Using copy)
import copy

class Point:
    def __init__(self, x):
        self.x = x

p1 = Point(10)
p2 = copy.copy(p1)
print(p2.x)
# ✅ Use Case:
# Useful in simulations or testing where you want to manipulate object state temporarily.
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


# Protected Attributes and Methods
# Protected attributes (with a single underscore _) can be accessed from outside the class and 
# by subclasses — but by convention, they are meant to be internal.

# Private attributes (with double underscore __) cannot be directly accessed outside the class or 
# in a subclass — they are name-mangled to prevent accidental access.
# 🧩 Syntax: _single_underscore
class Database:
    def __init__(self):
        self._connection = "db://..."  # protected

    def _connect(self):
        print("Connecting to DB...")
# This is a convention: “Don’t access me directly unless you’re subclassing.”

# It's not enforced by Python (can still access from outside).

# ✅ Use Case:
# Used when:

# The attribute is for internal logic of the class or frameworks.

# But subclasses might still need access.

class MySQLDatabase(Database):
    def reconnect(self):
        print("Reusing:", self._connection)
# You’ll see this a lot in Django/Flask/ORM internals — e.g., _meta, _fields, _execute()
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------



# Private Attributes and Methods
# 🔐 Syntax: __double_underscore
class Animal:
    def __init__(self):
        self.__type = "Wild"  # private

class Dog(Animal):
    def print_type(self):
        # print(self.__type)  ❌ This will raise AttributeError
        print(self._Animal__type)  # ✅ Accessible via name mangling
# Makes it harder to access/modify from outside.

# ✅ Use Case:
# Use when:

# You want to hide sensitive data or critical internal logic.

# Prevent subclass or user from accidentally changing the value.

# You’re writing security-sensitive modules like auth, token validation, crypto.

def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)