# Python Classes and Objects

# 1.Object-Oriented Programming (OOP)

Object-Oriented Programming is a programming style based on objects and classes.

It helps in:

- Organizing code better
- Reusability
- Real-world modeling
- Easier maintenance

Python is an object-oriented language.

---

# 2. What is a Class?

A class is a blueprint or template for creating objects.

It defines:

- Attributes (data)
- Methods (functions)

Example:

Think of a class like a "Car design".

---

# 3. What is an Object?

An object is an instance of a class.

Example:

If "Car" is a class, then:

- BMW
- Audi
- Tesla

are objects.

---

# 4. Creating a Class in Python

Syntax:

```python
class ClassName:
    pass
```

Example:

```python
class Student:
    pass
```

---

# 5. Creating Objects

Syntax:

```python
obj = ClassName()
```

Example:

```python
s1 = Student()
print(s1)
```

---

# 6. Attributes in Class

Attributes are variables inside a class.

## 6.1 Instance Attributes

Defined inside methods using `self`.

Example:

```python
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
```

---

# 7. The __init__ Method (Constructor)

The constructor is automatically called when an object is created.

Example:

```python
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

s1 = Student("Kirti", 20)
```

---

# 8. self Keyword

`self` represents the current object.

Example:

```python
class Student:
    def __init__(self, name):
        self.name = name

    def show(self):
        print(self.name)
```

---

# 9. Methods in Class

Methods are functions inside a class.

Example:

```python
class Student:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print("Hello", self.name)
```

Usage:

```python
s1 = Student("Kirti")
s1.greet()
```

Output:

```text
Hello Kirti
```

---

# 10. Instance vs Class Variables

## Instance Variable

Unique for each object.

```python
self.name = name
```

## Class Variable

Shared among all objects.

```python
class Student:
    college = "ABC College"
```

Example:

```python
class Student:
    college = "ABC College"

    def __init__(self, name):
        self.name = name

s1 = Student("A")
s2 = Student("B")

print(s1.college)
print(s2.college)
```

---

# 11. Accessing Attributes

```python
print(s1.name)
```

---

# 12. Modifying Attributes

```python
s1.name = "New Name"
```

---

# 13. Deleting Attributes

```python
del s1.name
```

---

# 14. Deleting Objects

```python
del s1
```

---

# 15. Multiple Objects

```python
class Student:
    def __init__(self, name):
        self.name = name

s1 = Student("A")
s2 = Student("B")

print(s1.name)
print(s2.name)
```

---

# 16. Object Methods Example

```python
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def show(self):
        print(self.name, self.marks)

    def is_pass(self):
        if self.marks >= 40:
            print("Pass")
        else:
            print("Fail")

s1 = Student("Kirti", 85)
s1.show()
s1.is_pass()
```

---

# 17. Passing Object as Parameter

```python
class Student:
    def __init__(self, name):
        self.name = name

def show_student(student):
    print(student.name)

s1 = Student("Kirti")
show_student(s1)
```

---

# 18. Returning Objects from Methods

```python
class Student:
    def __init__(self, name):
        self.name = name

    def update(self):
        return Student("Updated Name")

s1 = Student("Kirti")
s2 = s1.update()

print(s2.name)
```

---

# 19. Encapsulation (Basic Idea)

Encapsulation means hiding internal data.

Example:

```python
class Student:
    def __init__(self, name):
        self.__name = name  # private variable
```

Access:

```python
# Not directly accessible
```

Getter method:

```python
def get_name(self):
    return self.__name
```

---

# 20. Getter and Setter Methods

```python
class Student:
    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name
```

---

# 21. Constructor Overloading (Python Style)

Python does not support true overloading.

We use default parameters:

```python
class Student:
    def __init__(self, name=None):
        self.name = name
```

---

# 22. Destructor

Automatically called when object is deleted.

```python
class Student:
    def __init__(self):
        print("Object created")

    def __del__(self):
        print("Object deleted")

s1 = Student()
del s1
```

---

# 23. Class Method (@classmethod)

Operates on class variables.

```python
class Student:
    college = "ABC"

    @classmethod
    def change_college(cls, name):
        cls.college = name
```

---

# 24. Static Method (@staticmethod)

Does not use self or cls.

```python
class Math:
    @staticmethod
    def add(a, b):
        return a + b
```

---

# 25. Inheritance (Intro)

One class inherits another.

```python
class Parent:
    def show(self):
        print("Parent class")

class Child(Parent):
    pass

c = Child()
c.show()
```

---

# 26. Types of Inheritance

- Single
- Multiple
- Multilevel
- Hierarchical

---

# 27. Important Interview Example

```python
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print(self.name, self.marks)

    def is_topper(self):
        return self.marks > 90
```

---

# 28. Real World Mapping

| Real World | Python |
|------------|--------|
| Student | Class |
| Kirti | Object |
| Name/Age | Attributes |
| Study() | Method |

---

# 29. Key Interview Questions

Q1. What is difference between class and object?

Class = blueprint  
Object = instance

---

Q2. What is self?

Represents current object.

---

Q3. Why __init__ is used?

To initialize object data.

---

Q4. Difference between instance and class variable?

Instance → object specific  
Class → shared

---

Q5. Can Python support multiple constructors?

No, but default arguments simulate it.

---

# 30. Quick Revision

Class:

```python
class A:
    pass
```

Object:

```python
a = A()
```

Constructor:

```python
def __init__(self):
```

Method:

```python
def show(self):
```

Class variable:

```python
class A:
    x = 10
```

Static method:

```python
@staticmethod
```

Class method:

```python
@classmethod
```