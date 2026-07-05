# TOPICS REVISED OR LEARNT - DAY 3

'''
1. What are Loops?

Loops are used to execute a block of code repeatedly.

Instead of writing the same code multiple times,
we can use loops.


2. Types of Loops in Python

a) for loop

b) while loop


3. for Loop

Used when the number of iterations is known.

Syntax:

for variable in sequence:
    code

'''

for i in range(5):
    print(i)

# Output:
# 0 1 2 3 4


'''
4. range()

Most commonly used with for loops.

range(stop)

range(start, stop)

range(start, stop,step)

'''

print(list(range(5)))

# [0, 1, 2, 3, 4]


print(list(range(1,10)))

# [1,2,3,4,5,6,7,8,9]


print(list(range(1,10,2)))

# [1,3,5,7,9]


'''
5. Looping Through a String

Strings are iterable.

'''

name= "Python"

for ch in name:
    print(ch)



'''
6. Looping Through a List

'''

nums= [10,20,30,40]

for num in nums:
    print(num)



'''
7. Using _ in Loops

Used when loop variable is not required.

'''

for _ in range(3):
    print("Hello")



'''
8. Nested for Loops

Loop inside another loop.

Very important for patterns.

'''

for i in range(3):
    for j in range(3):
        
        print(i,j)



'''
9. while Loop

Used when number of iterations is unknown.

Runs until condition becomes False.

Syntax:

while condition:
    code

'''

count = 1
while count <= 5:

    print(count)

    count += 1



'''
10. Infinite Loop

A loop that never ends.

'''

# while True:
#     print("Running")


'''
11. Importance of Updating Variable

Without updating the variable,
the loop may become infinite.

'''

count = 1

while count <= 5:

    print(count)

    count += 1



'''
12. Difference Between for and while

for loop:

Used when iterations are known.

while loop:

Used when condition controls execution.

'''


'''
13. break Statement

Immediately terminates loop.

Very important interview topic.

'''

for i in range(1,11):

    if i == 5:
        break

    print(i)

# Output:
# 1 2 3 4



'''
14. continue Statement

Skips current iteration.

Moves to next iteration.

'''

for i in range(1,6):

    if i == 3:
        continue

    print(i)

# Output:
# 1 2 4 5



'''
15. pass Statement

Placeholder.

Does nothing.

'''

for i in range(5):

    pass



'''
16. break vs continue

break

→ exits entire loop

continue

→ skips only current iteration

'''



'''
17. else with Loops

The else block executes only if loop
finishes normally.

If break occurs,
else will not execute.

'''

for i in range(5):

    print(i)

else:

    print("Loop Finished")



'''
18. for-else Example

'''

for i in range(5):

    if i == 10:
        break

else:

    print("Value Not Found")



'''
19. while-else Example

'''

count = 1

while count <= 3:

    print(count)

    count += 1

else:

    print("Loop Ended Successfully")



'''
20. Iterating Using Index

Sometimes index is required.

'''

fruits = ["Apple","Banana","Mango"]

for i in range(len(fruits)):

    print(i, fruits[i])



'''
21. enumerate()

Cleaner way to access index and value.

'''

fruits = ["Apple","Banana","Mango"]

for index, value in enumerate(fruits):

    print(index, value)



'''
22. Reversing a Loop

'''

for i in range(10,0,-1):

    print(i)

# 10 to 1



'''
23. Sum of First N Numbers

Classic Interview Question

'''

n = 5

total = 0

for i in range(1,n+1):

    total += i

print(total)



'''
24. Count Even Numbers

'''

count = 0

for i in range(1,11):

    if i % 2 == 0:

        count += 1

print(count)



'''
25. Factorial Using Loop

Important Interview Question

'''

n = 5

fact = 1

for i in range(1,n+1):

    fact *= i

print(fact)



'''
26. Common Mistake

range(5)

Produces:

0 1 2 3 4

NOT

1 2 3 4 5

'''




'''
27. Common Mistake

Forgetting += 1 in while loop.

Can cause infinite loop.

'''




'''
28. Pattern Printing Basics

Outer loop

→ rows

Inner loop

→ columns

'''

for i in range(3):

    for j in range(3):

        print("*", end=" ")

    print()



'''
Output

* * *
* * *
* * *

'''




'''
29. Time Complexity of Loops

Single Loop

O(n)

Nested Loop

O(n²)

Three Nested Loops

O(n³)

Important for interviews.

'''




'''
30. Interview Questions


Q1. Difference between for and while loop?

for:
Used when iterations are known.

while:
Used when condition controls execution.



Q2. Difference between break and continue?

break:
Terminates loop completely.

continue:
Skips current iteration only.



Q3. What is an infinite loop?

A loop that never becomes False.

Example:

while True:
    pass



Q4. What is loop else?

The else block executes if loop finishes normally.

Not executed when break occurs.



Q5. What is the output?

for i in range(5):
    print(i)

Output:

0
1
2
3
4



Q6. What is the output?

for i in range(5):

    if i == 2:
        continue

    print(i)

Output:

0
1
3
4



Q7. What is the output?

for i in range(5):

    if i == 2:
        break

    print(i)

Output:

0
1



Q8. Why is enumerate() preferred?

Because it provides both index and value
without manually using range(len()).



Q9. What is the time complexity of a single loop?

O(n)



Q10. What is the time complexity of two nested loops?

O(n²)



Q11. What is the most common mistake in while loops?

Forgetting to update the loop variable,
causing an infinite loop.



Q12. Which loop is better?

Neither.

Use for when count is known.

Use while when condition controls execution.



Q13. What will be the output?

for i in range(1,5):
    print(i)

Output:

1
2
3
4

(stop value excluded)



Q14. What is range(1,10,2)?

Output:

1
3
5
7
9



Q15. Why are nested loops important?

Used in:

Pattern Printing

Matrices

Tables

Grid Problems

2D Arrays

Many DSA Problems


Next Topic:

Functions
(User Defined Functions, Parameters,
Arguments, Return Statement,
Lambda Functions, Recursion,
Scope, *args, **kwargs)
'''