# ==========================================================
#                 PYTHON INHERITANCE NOTES
# ==========================================================

# 1. What is Inheritance?
#
# Inheritance is an OOP concept where one class acquires
# the properties and methods of another class.
#
# It promotes:
# - Code Reusability
# - Better Organization
# - Easier Maintenance
#

# ----------------------------------------------------------

# Basic Inheritance

class Animal:

    def eat(self):
        print("Animal is eating")


class Dog(Animal):
    pass


d = Dog()

d.eat()

# Output:
# Animal is eating

# ----------------------------------------------------------

# Child Class Accessing Parent Methods

class Vehicle:

    def start(self):
        print("Vehicle Started")


class Car(Vehicle):
    pass


c = Car()

c.start()

# ----------------------------------------------------------

# Parent with Constructor

class Animal:

    def __init__(self):
        print("Animal Constructor")

    def sound(self):
        print("Animal makes sound")


class Dog(Animal):
    pass


d = Dog()

# Output:
# Animal Constructor

# ----------------------------------------------------------

# Child Having Its Own Constructor

class Animal:

    def __init__(self):
        print("Animal Constructor")


class Dog(Animal):

    def __init__(self):
        print("Dog Constructor")


d = Dog()

# Output:
# Dog Constructor
#
# Parent constructor is NOT called automatically
# if child has its own constructor.

# ----------------------------------------------------------

# Using super() to Call Parent Constructor

class Animal:

    def __init__(self):
        print("Animal Constructor")


class Dog(Animal):

    def __init__(self):
        super().__init__()
        print("Dog Constructor")


d = Dog()

# Output:
# Animal Constructor
# Dog Constructor

# ----------------------------------------------------------

# Child Class Adding New Methods

class Animal:

    def eat(self):
        print("Eating...")


class Dog(Animal):

    def bark(self):
        print("Barking...")


d = Dog()

d.eat()
d.bark()

# ----------------------------------------------------------

# Method Overriding
#
# Child class provides its own implementation
# of the parent's method.

class Animal:

    def sound(self):
        print("Animal Sound")


class Dog(Animal):

    def sound(self):
        print("Bark")


d = Dog()

d.sound()

# Output:
# Bark

# ----------------------------------------------------------

# Using super() Inside Overridden Method

class Animal:

    def sound(self):
        print("Animal Sound")


class Dog(Animal):

    def sound(self):
        super().sound()
        print("Dog Bark")


d = Dog()

d.sound()

# Output:
# Animal Sound
# Dog Bark

# ----------------------------------------------------------

# Types of Inheritance

# 1. Single Inheritance

class A:

    def display(self):
        print("Class A")


class B(A):
    pass


obj = B()
obj.display()

# ----------------------------------------------------------

# 2. Multilevel Inheritance

class A:

    def show(self):
        print("Class A")


class B(A):
    pass


class C(B):
    pass


obj = C()

obj.show()

# ----------------------------------------------------------

# 3. Multiple Inheritance

class Father:

    def skills1(self):
        print("Driving")


class Mother:

    def skills2(self):
        print("Cooking")


class Child(Father, Mother):
    pass


obj = Child()

obj.skills1()
obj.skills2()

# ----------------------------------------------------------

# 4. Hierarchical Inheritance

class Parent:

    def display(self):
        print("Parent Class")


class Child1(Parent):
    pass


class Child2(Parent):
    pass


c1 = Child1()
c2 = Child2()

c1.display()
c2.display()

# ----------------------------------------------------------

# isinstance()
#
# Checks whether an object belongs to a class.

class Animal:
    pass


class Dog(Animal):
    pass


d = Dog()

print(isinstance(d, Dog))
print(isinstance(d, Animal))

# Output:
# True
# True

# ----------------------------------------------------------

# issubclass()
#
# Checks whether one class inherits another.

class Animal:
    pass


class Dog(Animal):
    pass


print(issubclass(Dog, Animal))
print(issubclass(Animal, Dog))

# Output:
# True
# False

# ----------------------------------------------------------

# Accessing Parent Method Using Child Object

class Person:

    def greet(self):
        print("Hello")


class Student(Person):
    pass


s = Student()

s.greet()

# ----------------------------------------------------------

# Real Life Example

class Employee:

    def work(self):
        print("Employee is working")


class Manager(Employee):

    def manage(self):
        print("Manager manages the team")


m = Manager()

m.work()
m.manage()

# ----------------------------------------------------------

# Advantages of Inheritance
#
# 1. Code Reusability
# 2. Reduces Code Duplication
# 3. Easier Maintenance
# 4. Improves Readability
# 5. Supports Method Overriding
# 6. Makes Programs More Organized

# ----------------------------------------------------------

# Common Interview Questions
#
# Q1. What is inheritance?
# It is the process by which one class acquires
# the properties and methods of another class.
#
# Q2. What is a parent class?
# The class whose properties are inherited.
#
# Q3. What is a child class?
# The class that inherits from another class.
#
# Q4. What is method overriding?
# Redefining a parent class method in the child class.
#
# Q5. What does super() do?
# It allows access to the parent class's methods
# and constructor.
#
# Q6. How many types of inheritance are supported in Python?
# - Single
# - Multiple
# - Multilevel
# - Hierarchical
#
# (Python does not directly support Hybrid Inheritance
# as a separate type, but it can be achieved using a
# combination of the above.)

# ----------------------------------------------------------

# Quick Revision
#
# Syntax:
#
# class Child(Parent):
#     pass
#
# Parent Constructor:
# super().__init__()
#
# Parent Method:
# super().method()
#
# Method Overriding:
# Child defines the same method as Parent.
#
# Check Object Type:
# isinstance(obj, ClassName)
#
# Check Class Relationship:
# issubclass(Child, Parent)
#
# Types:
# 1. Single
# 2. Multiple
# 3. Multilevel
# 4. Hierarchical