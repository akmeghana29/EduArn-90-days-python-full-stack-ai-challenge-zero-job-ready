# ==========================================================
#                 PYTHON POLYMORPHISM
# ==========================================================

# 1. What is Polymorphism?
#
# Polymorphism means "many forms".
#
# It allows the same method, function or operator
# to behave differently depending on the object or data.
#
# Poly = Many
# Morph = Forms
#
# Example:
# A person can be a Student, Employee, Teacher, etc.
# Same person, different roles.

# ----------------------------------------------------------

# 2. Function Polymorphism
#
# The same function works with different data types.

print(len("Kirti"))          # String
print(len([1, 2, 3]))        # List
print(len((1, 2, 3, 4)))     # Tuple
print(len({"a": 1, "b": 2})) # Dictionary

# Output:
# 6
# 3
# 4
# 2

# ----------------------------------------------------------

# 3. Operator Polymorphism
#
# The '+' operator behaves differently depending
# on the operands.

print(10 + 20)

print("Hello " + "World")

print([1, 2] + [3, 4])

# Output:
# 30
# Hello World
# [1, 2, 3, 4]

# ----------------------------------------------------------

# 4. Method Polymorphism
#
# Different classes can have methods with the same name.

class Dog:

    def sound(self):
        print("Dog barks")


class Cat:

    def sound(self):
        print("Cat meows")


d = Dog()
c = Cat()

d.sound()
c.sound()

# ----------------------------------------------------------

# 5. Polymorphism Using a Common Function

class Dog:

    def sound(self):
        print("Dog barks")


class Cat:

    def sound(self):
        print("Cat meows")


def animal_sound(animal):
    animal.sound()


animal_sound(Dog())
animal_sound(Cat())

# Output:
# Dog barks
# Cat meows

# ----------------------------------------------------------

# 6. Polymorphism with Inheritance

class Animal:

    def sound(self):
        print("Animal makes a sound")


class Dog(Animal):

    def sound(self):
        print("Dog barks")


class Cat(Animal):

    def sound(self):
        print("Cat meows")


a = Animal()
d = Dog()
c = Cat()

a.sound()
d.sound()
c.sound()

# ----------------------------------------------------------

# 7. Method Overriding
#
# Child class provides its own implementation
# of the parent's method.

class Vehicle:

    def start(self):
        print("Vehicle Started")


class Car(Vehicle):

    def start(self):
        print("Car Started")


v = Vehicle()
c = Car()

v.start()
c.start()

# ----------------------------------------------------------

# 8. Using super() with Polymorphism

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

# 9. Duck Typing
#
# In Python, if an object behaves like what is expected,
# it can be used regardless of its actual type.
#
# "If it walks like a duck and quacks like a duck,
# it is treated as a duck."

class Bird:

    def fly(self):
        print("Bird is flying")


class Airplane:

    def fly(self):
        print("Airplane is flying")


def start_flying(obj):
    obj.fly()


start_flying(Bird())
start_flying(Airplane())

# ----------------------------------------------------------

# 10. Method Overloading
#
# Python does NOT support true method overloading.
#
# Defining multiple methods with the same name
# replaces the previous method.

# Wrong

# class Demo:
#
#     def add(self, a):
#         pass
#
#     def add(self, a, b):
#         pass

# Only the second method exists.

# ----------------------------------------------------------

# 11. Simulating Method Overloading
#
# Use default arguments.

class Calculator:

    def add(self, a, b=0):
        return a + b


obj = Calculator()

print(obj.add(10))
print(obj.add(10, 20))

# Output:
# 10
# 30

# ----------------------------------------------------------

# Using *args

class Calculator:

    def add(self, *numbers):
        return sum(numbers)


obj = Calculator()

print(obj.add(5))
print(obj.add(5, 10))
print(obj.add(5, 10, 15))

# ----------------------------------------------------------

# 12. Built-in Polymorphism Examples

print(abs(-10))

print(max(10, 20, 30))

print(min(5, 2, 9))

print(round(4.76))

# Same functions work with different values.

# ----------------------------------------------------------

# 13. Real Life Example

class Payment:

    def pay(self):
        print("Payment Done")


class CreditCard(Payment):

    def pay(self):
        print("Paid using Credit Card")


class UPI(Payment):

    def pay(self):
        print("Paid using UPI")


class Cash(Payment):

    def pay(self):
        print("Paid using Cash")


payments = [CreditCard(), UPI(), Cash()]

for method in payments:
    method.pay()

# ----------------------------------------------------------

# Advantages of Polymorphism
#
# 1. Code Reusability
# 2. Flexible Programs
# 3. Easy to Extend
# 4. Cleaner Code
# 5. Less Conditional Logic
# 6. Better Maintainability

# ----------------------------------------------------------

# Common Interview Questions
#
# Q1. What is polymorphism?
# One interface, many implementations.
#
# Q2. What are the types of polymorphism?
# - Compile-time Polymorphism
# - Runtime Polymorphism
#
# Note:
# Python mainly supports Runtime Polymorphism.
#
# Q3. What is method overriding?
# Redefining a parent class method in the child class.
#
# Q4. Does Python support method overloading?
# No.
# It can be simulated using:
# - Default arguments
# - *args
# - **kwargs
#
# Q5. What is Duck Typing?
# If an object has the required method or behavior,
# Python allows it to be used without checking its type.

# ----------------------------------------------------------

# Quick Revision
#
# Polymorphism = One Interface, Many Forms
#
# Function Polymorphism
# len()
#
# Operator Polymorphism
# +
#
# Runtime Polymorphism
# Method Overriding
#
# Duck Typing
# Object behavior matters, not its type.
#
# Method Overloading
# Not supported directly.
#
# Simulate Overloading
# - Default Parameters
# - *args
# - **kwargs
#
# Parent Method
# super().method()