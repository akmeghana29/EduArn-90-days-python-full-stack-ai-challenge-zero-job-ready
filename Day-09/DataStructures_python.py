# Python Collections Master Notes

# 1. Lists

## Definition
A list is an ordered, mutable collection that can store multiple values.

```python
nums = [10, 20, 30]
```

## Characteristics
- Ordered
- Mutable
- Allows duplicates
- Supports indexing
- Can store mixed data types

```python
data = [1, "Hello", 3.5, True]
```

## Creating Lists

```python
a = []
b = list()
c = [1, 2, 3]
```

## Accessing Elements

```python
nums = [10, 20, 30, 40]

nums[0]
nums[-1]
```

## Slicing

```python
nums[1:4]
nums[:3]
nums[::2]
nums[::-1]
```

## Updating Elements

```python
nums[0] = 100
```

## Adding Elements

### append()

```python
nums.append(50)
```

### insert()

```python
nums.insert(1, 99)
```

### extend()

```python
nums.extend([60, 70])
```

## Removing Elements

### remove()

```python
nums.remove(20)
```

### pop()

```python
nums.pop()
nums.pop(2)
```

### del

```python
del nums[0]
```

### clear()

```python
nums.clear()
```

## Searching

### index()

```python
nums.index(30)
```

### count()

```python
nums.count(10)
```

## Sorting

### sort()

```python
nums.sort()
nums.sort(reverse=True)
```

### sorted()

```python
new_list = sorted(nums)
```

## Reverse

```python
nums.reverse()
```

## Copying Lists

```python
copy1 = nums.copy()
copy2 = nums[:]
```

## Membership

```python
10 in nums
20 not in nums
```

## Iteration

```python
for item in nums:
    print(item)
```

```python
for index, value in enumerate(nums):
    print(index, value)
```

## List Comprehension

```python
squares = [x*x for x in range(5)]
```

```python
evens = [x for x in range(10) if x % 2 == 0]
```

## Nested Lists

```python
matrix = [
    [1, 2],
    [3, 4]
]
```

## Built-in Functions

```python
len(nums)
max(nums)
min(nums)
sum(nums)
```

## Time Complexity

| Operation | Complexity |
|------------|------------|
| Access | O(1) |
| Search | O(n) |
| Append | O(1) |
| Insert | O(n) |
| Delete | O(n) |

---

# 2. Tuples

## Definition

Tuple is an ordered immutable collection.

```python
t = (1, 2, 3)
```

## Characteristics

- Ordered
- Immutable
- Allows duplicates
- Faster than lists

## Creating Tuples

```python
t1 = ()
t2 = (1, 2, 3)
t3 = 1, 2, 3
```

### Single Element Tuple

```python
t = (5,)
```

## Accessing Elements

```python
t[0]
t[-1]
```

## Slicing

```python
t[1:3]
```

## Tuple Methods

### count()

```python
t.count(2)
```

### index()

```python
t.index(3)
```

## Tuple Packing

```python
t = 1, 2, 3
```

## Tuple Unpacking

```python
a, b, c = t
```

## Swapping

```python
a, b = b, a
```

## Nested Tuple

```python
t = ((1, 2), (3, 4))
```

## Built-in Functions

```python
len(t)
max(t)
min(t)
sum(t)
```

## Time Complexity

| Operation | Complexity |
|------------|------------|
| Access | O(1) |
| Search | O(n) |

---

# 3. Sets

## Definition

Set is an unordered collection of unique elements.

```python
s = {1, 2, 3}
```

## Characteristics

- Unordered
- Mutable
- No duplicates
- Fast lookup

## Creating Sets

```python
s = {1, 2, 3}
```

```python
s = set([1, 2, 2, 3])
```

## Empty Set

```python
s = set()
```

## Adding Elements

### add()

```python
s.add(10)
```

### update()

```python
s.update([20, 30])
```

## Removing Elements

### remove()

```python
s.remove(10)
```

### discard()

```python
s.discard(10)
```

### pop()

```python
s.pop()
```

### clear()

```python
s.clear()
```

## Membership

```python
10 in s
```

## Set Operations

```python
A = {1, 2, 3}
B = {3, 4, 5}
```

### Union

```python
A | B
A.union(B)
```

### Intersection

```python
A & B
A.intersection(B)
```

### Difference

```python
A - B
```

### Symmetric Difference

```python
A ^ B
```

## Relationship Methods

### issubset()

```python
A.issubset(B)
```

### issuperset()

```python
A.issuperset(B)
```

### isdisjoint()

```python
A.isdisjoint(B)
```

## Frozen Set

Immutable version of set.

```python
fs = frozenset([1, 2, 3])
```

## Time Complexity

| Operation | Complexity |
|------------|------------|
| Add | O(1) |
| Remove | O(1) |
| Search | O(1) |

---

# 4. Dictionaries

## Definition

Dictionary stores data in key-value pairs.

```python
student = {
    "name": "Kirti",
    "age": 21
}
```

## Characteristics

- Mutable
- Key-value structure
- Keys must be unique
- Fast lookup

## Creating Dictionaries

```python
d = {}
```

```python
d = dict()
```

```python
d = {
    "name": "Kirti",
    "age": 21
}
```

## Accessing Values

### Bracket Notation

```python
d["name"]
```

### get()

```python
d.get("name")
```

## Adding Elements

```python
d["city"] = "Delhi"
```

## Updating Elements

```python
d["age"] = 22
```

## Removing Elements

### pop()

```python
d.pop("age")
```

### del

```python
del d["name"]
```

### clear()

```python
d.clear()
```

## Dictionary Methods

### keys()

```python
d.keys()
```

### values()

```python
d.values()
```

### items()

```python
d.items()
```

### update()

```python
d.update({"age": 22})
```

### setdefault()

```python
d.setdefault("city", "Delhi")
```

## Looping

### Keys

```python
for key in d:
    print(key)
```

### Values

```python
for value in d.values():
    print(value)
```

### Key-Value Pairs

```python
for key, value in d.items():
    print(key, value)
```

## Dictionary Comprehension

```python
squares = {x: x*x for x in range(5)}
```

## Nested Dictionary

```python
student = {
    "name": "Kirti",
    "marks": {
        "math": 90,
        "cs": 95
    }
}
```

## Time Complexity

| Operation | Complexity |
|------------|------------|
| Access | O(1) |
| Insert | O(1) |
| Delete | O(1) |
| Search | O(1) |

---

# Quick Comparison

| Feature | List | Tuple | Set | Dictionary |
|----------|--------|--------|--------|------------|
| Ordered | Yes | Yes | No | Yes |
| Mutable | Yes | No | Yes | Yes |
| Duplicates | Yes | Yes | No | Keys No |
| Indexed | Yes | Yes | No | Key-based |
| Syntax | [] | () | {} | {k:v} |

---

# Interview Cheatsheet

## Use List When
- Order matters
- Frequent modifications
- Index access required

## Use Tuple When
- Data should not change
- Fixed records
- Dictionary keys

## Use Set When
- Remove duplicates
- Fast lookup
- Mathematical set operations

## Use Dictionary When
- Key-value mapping
- Frequency counting
- Fast retrieval

## Most Common DSA Usage

### Frequency Count

```python
freq = {}

for num in nums:
    freq[num] = freq.get(num, 0) + 1
```

### Remove Duplicates

```python
unique = list(set(nums))
```

### Fast Lookup

```python
seen = set()

for num in nums:
    if num in seen:
        print("Found")
```