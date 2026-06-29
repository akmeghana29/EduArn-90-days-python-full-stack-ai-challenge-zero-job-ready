# ==========================================================
#            PYTHON CONSTRUCTORS
# ==========================================================

# 1. What is a Constructor?
#
# A constructor is a special method that is automatically
# called whenever an object is created.
#
# In Python, the constructor is:
#
# __init__()
#
# It is mainly used to initialize instance variables.

# ----------------------------------------------------------

# Basic Constructor Example

class Student:

    def __init__(self):
        print("Constructor Called")


s1 = Student()

# Output:
# Constructor Called

# ----------------------------------------------------------

# Parameterized Constructor
#
# A constructor can accept parameters to initialize
# object attributes.

class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age


s1 = Student("Kirti", 21)

print(s1.name)
print(s1.age)

# Output:
# Kirti
# 21

# ----------------------------------------------------------

# self Keyword
#
# self refers to the current object.
#
# self.name -> instance variable
# name -> constructor parameter

class Student:

    def __init__(self, name):
        self.name = name


s1 = Student("Kirti")
print(s1.name)

# ----------------------------------------------------------

# Multiple Objects
#
# Every object gets its own copy of instance variables.

class Student:

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks


s1 = Student("Kirti", 90)
s2 = Student("Rahul", 75)

print(s1.name, s1.marks)
print(s2.name, s2.marks)

# ----------------------------------------------------------

# Constructor with Default Values

class Student:

    def __init__(self, name="Unknown", marks=0):
        self.name = name
        self.marks = marks


s1 = Student()
s2 = Student("Kirti", 95)

print(s1.name, s1.marks)
print(s2.name, s2.marks)

# ----------------------------------------------------------

# Constructor with Optional Arguments

class Employee:

    def __init__(self, name, salary=25000):
        self.name = name
        self.salary = salary


e1 = Employee("Aman")
e2 = Employee("Kirti", 50000)

print(e1.salary)
print(e2.salary)

# ----------------------------------------------------------

# Types of Constructors
#
# 1. Default Constructor
# 2. Parameterized Constructor

# Default Constructor

class Demo:

    def __init__(self):
        print("Default Constructor")


d = Demo()

# ----------------------------------------------------------

# Parameterized Constructor

class Demo:

    def __init__(self, x):
        self.x = x


d = Demo(100)
print(d.x)

# ----------------------------------------------------------

# Constructor Overloading
#
# Python does NOT support multiple constructors.
#
# This is NOT allowed:
#
# def __init__(self):
#     ...
#
# def __init__(self, name):
#     ...
#
# Only the last one will exist.

# Instead, use default values.

class Student:

    def __init__(self, name="Unknown", age=0):
        self.name = name
        self.age = age


s = Student()
print(s.name, s.age)

# ----------------------------------------------------------

# Calling Another Method from Constructor

class Student:

    def __init__(self, name):
        self.name = name
        self.display()

    def display(self):
        print("Student Name:", self.name)


s = Student("Kirti")

# ----------------------------------------------------------

# Class Variable + Constructor

class Student:

    college = "ABC College"

    def __init__(self, name):
        self.name = name


s = Student("Kirti")

print(s.name)
print(s.college)

# ----------------------------------------------------------

# Constructor vs Normal Method
#
# Constructor:
# Automatically called when object is created.
#
# Normal Method:
# Called manually using object.method()

class Student:

    def __init__(self):
        print("Constructor")

    def show(self):
        print("Normal Method")


s = Student()
s.show()

# ----------------------------------------------------------

# Destructor
#
# __del__() is called when an object is destroyed.

class Student:

    def __init__(self):
        print("Object Created")

    def __del__(self):
        print("Object Destroyed")


s = Student()

del s

# ----------------------------------------------------------

# Common Mistakes

# Wrong
#
# class Student:
#     def __init__(name):
#         pass

# Correct

class Student:

    def __init__(self, name):
        self.name = name

# ----------------------------------------------------------

# Wrong

# class Student:
#
#     def __init__(self, name):
#         name = name

# Correct

class Student:

    def __init__(self, name):
        self.name = name

# ----------------------------------------------------------

# Interview Questions
#
# Q1. What is a constructor?
# A special method that runs automatically when an object is created.
#
# Q2. Name of Python constructor?
# __init__()
#
# Q3. Can Python have multiple constructors?
# No.
#
# Q4. How do we simulate constructor overloading?
# Using default arguments, *args or **kwargs.
#
# Q5. What is self?
# It refers to the current object.

# ----------------------------------------------------------

# Quick Revision
#
# Constructor
# def __init__(self):
#
# Parameterized Constructor
# def __init__(self, name):
#
# Instance Variable
# self.name = name
#
# Object Creation
# obj = ClassName(...)
#
# Destructor
# def __del__(self):