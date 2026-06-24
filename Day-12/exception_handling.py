# Python Exception Handling (try/except) 

# 1. What is an Exception?

An exception is a runtime error that interrupts the normal flow of a program.

Examples:

- Dividing by zero
- Accessing an invalid list index
- Opening a non-existent file
- Converting invalid strings to integers

Example:

```python
print(10 / 0)
```

Output:

```python
ZeroDivisionError: division by zero
```

Without exception handling, the program terminates immediately.

---

# 2. Why Exception Handling?

Benefits:

- Prevent program crashes
- Handle errors gracefully
- Improve user experience
- Allow program continuation

Example:

Without exception handling:

```python
num = int(input("Enter number: "))
print(100 / num)
```

Input:

```text
0
```

Program crashes.

With exception handling:

```python
try:
    num = int(input("Enter number: "))
    print(100 / num)
except ZeroDivisionError:
    print("Cannot divide by zero")
```

Program continues safely.

---

# 3. try Block

The code that may generate an exception is placed inside the try block.

Syntax:

```python
try:
    risky_code
```

Example:

```python
try:
    print(10 / 0)
```

---

# 4. except Block

Handles the exception raised inside try.

Syntax:

```python
try:
    risky_code
except ExceptionType:
    handling_code
```

Example:

```python
try:
    print(10 / 0)
except ZeroDivisionError:
    print("Division by zero is not allowed")
```

Output:

```text
Division by zero is not allowed
```

---

# 5. Flow of Execution

```python
try:
    statement1
    statement2
    statement3
except Error:
    handler
```

Case 1: No Exception

```text
statement1
statement2
statement3
```

except block skipped.

Case 2: Exception Occurs

```text
statement1
Exception
```

Remaining try statements skipped.

Control jumps to except block.

---

# 6. Handling Multiple Exceptions

Example:

```python
try:
    num = int(input())
    print(10 / num)

except ValueError:
    print("Invalid number")

except ZeroDivisionError:
    print("Cannot divide by zero")
```

Possible Inputs:

```text
abc
```

Output:

```text
Invalid number
```

Input:

```text
0
```

Output:

```text
Cannot divide by zero
```

---

# 7. Multiple Exceptions in One except

Syntax:

```python
except (Exception1, Exception2):
```

Example:

```python
try:
    num = int(input())
    print(10 / num)

except (ValueError, ZeroDivisionError):
    print("Invalid operation")
```

---

# 8. Generic Exception Handler

Catches almost every exception.

Syntax:

```python
except Exception:
```

Example:

```python
try:
    x = int("abc")

except Exception:
    print("Some error occurred")
```

Output:

```text
Some error occurred
```

---

# 9. Capturing Error Message

Syntax:

```python
except Exception as e:
```

Example:

```python
try:
    print(10 / 0)

except Exception as e:
    print(e)
```

Output:

```text
division by zero
```

Another Example:

```python
try:
    int("abc")

except Exception as e:
    print(type(e))
    print(e)
```

Output:

```text
<class 'ValueError'>
invalid literal for int()
```

---

# 10. else Block

Runs only if NO exception occurs.

Syntax:

```python
try:
    risky_code

except:
    handler

else:
    success_code
```

Example:

```python
try:
    num = int(input())
    result = 10 / num

except ZeroDivisionError:
    print("Cannot divide")

else:
    print("Result =", result)
```

Input:

```text
2
```

Output:

```text
Result = 5.0
```

---

# 11. finally Block

Runs regardless of whether an exception occurs.

Syntax:

```python
try:
    pass

except:
    pass

finally:
    pass
```

Commonly used for:

- Closing files
- Closing database connections
- Releasing resources

Example:

```python
try:
    print(10 / 0)

except ZeroDivisionError:
    print("Error")

finally:
    print("Always executes")
```

Output:

```text
Error
Always executes
```

---

# 12. Complete Structure

```python
try:
    pass

except:
    pass

else:
    pass

finally:
    pass
```

Execution Order:

```text
try
↓
except (if needed)
↓
else (if no exception)
↓
finally
```

---

# 13. Common Built-in Exceptions

## ZeroDivisionError

```python
10 / 0
```

---

## ValueError

```python
int("abc")
```

---

## TypeError

```python
"5" + 5
```

---

## IndexError

```python
arr = [1, 2]
print(arr[5])
```

---

## KeyError

```python
d = {"a": 1}
print(d["b"])
```

---

## NameError

```python
print(x)
```

---

## FileNotFoundError

```python
open("abc.txt")
```

---

## AttributeError

```python
x = 10
x.append(5)
```

---

## ImportError

```python
import unknownmodule
```

---

## ModuleNotFoundError

```python
import xyzabc
```

---

# 14. Raising Exceptions Manually

Use raise keyword.

Syntax:

```python
raise ExceptionType("message")
```

Example:

```python
raise ValueError("Invalid input")
```

Output:

```text
ValueError: Invalid input
```

---

# 15. Why Raise Exceptions?

Used when custom validation fails.

Example:

```python
age = -5

if age < 0:
    raise ValueError("Age cannot be negative")
```

---

# 16. Re-Raising Exceptions

Example:

```python
try:
    print(10 / 0)

except ZeroDivisionError:
    print("Logging error")
    raise
```

Output:

```text
Logging error
ZeroDivisionError
```

Used when:

- Logging error
- Passing error upward

---

# 17. Custom Exceptions

Create your own exception class.

Syntax:

```python
class MyError(Exception):
    pass
```

Example:

```python
class InvalidAgeError(Exception):
    pass

age = -1

if age < 0:
    raise InvalidAgeError("Invalid age")
```

---

# 18. Custom Exception with Message

```python
class InvalidSalaryError(Exception):
    pass

salary = -500

if salary < 0:
    raise InvalidSalaryError("Salary cannot be negative")
```

---

# 19. Nested try Blocks

Example:

```python
try:
    try:
        print(10 / 0)

    except ZeroDivisionError:
        print("Inner Handler")

except:
    print("Outer Handler")
```

Output:

```text
Inner Handler
```

---

# 20. try-except Inside Loops

Example:

```python
while True:

    try:
        num = int(input("Enter Number: "))
        break

    except ValueError:
        print("Invalid Input")
```

Useful for input validation.

---

# 21. Using Exception Handling with Files

Example:

```python
try:
    with open("data.txt", "r") as file:
        print(file.read())

except FileNotFoundError:
    print("File not found")
```

---

# 22. Catching Multiple Exceptions Separately

```python
try:
    num = int(input())
    print(10 / num)

except ValueError:
    print("Invalid number")

except ZeroDivisionError:
    print("Division by zero")
```

---

# 23. Catching All Exceptions

```python
try:
    risky_code()

except Exception as e:
    print("Error:", e)
```

Useful for debugging.

Not recommended as the only exception handler in production.

---

# 24. Best Practices

Catch specific exceptions:

Good:

```python
except ValueError:
```

Bad:

```python
except:
```

Use finally for cleanup:

```python
finally:
    file.close()
```

Use custom exceptions for business logic.

Do not suppress errors silently:

Bad:

```python
except:
    pass
```

Always log or handle appropriately.

---

# 25. Exception Hierarchy 

```text
BaseException
│
├── Exception
│   ├── ValueError
│   ├── TypeError
│   ├── IndexError
│   ├── KeyError
│   ├── NameError
│   ├── FileNotFoundError
│   ├── AttributeError
│   └── ZeroDivisionError
│
├── KeyboardInterrupt
└── SystemExit
```

Most user-defined exceptions inherit from Exception.

---

# 26. Interview Questions

Q1. Difference between Error and Exception?

Error:
- Serious problem
- Usually not handled

Exception:
- Runtime issue
- Can be handled

---

Q2. Difference between except and finally?

except:
- Executes only when exception occurs

finally:
- Executes always

---

Q3. Difference between raise and except?

raise:
- Creates exception

except:
- Handles exception

---

Q4. Difference between Exception and BaseException?

Exception:
- Parent of most application exceptions

BaseException:
- Top-level parent of all exceptions

---

Q5. Can try exist without except?

Yes.

```python
try:
    pass
finally:
    pass
```

Valid.

---

# Revision

Basic:

```python
try:
    pass
except:
    pass
```

Capture Error:

```python
except Exception as e:
```

Multiple Exceptions:

```python
except (ValueError, TypeError):
```

Else:

```python
else:
```

Finally:

```python
finally:
```

Raise Exception:

```python
raise ValueError("Error")
```

Custom Exception:

```python
class MyError(Exception):
    pass
```

File Handling:

```python
try:
    with open("file.txt") as f:
        pass
except FileNotFoundError:
    pass
```