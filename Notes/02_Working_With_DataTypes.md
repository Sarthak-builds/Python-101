# Python Data Types and Memory Management

## Introduction to Python's Memory Model
In Python, everything is an object. This means that every value you work with—whether it's a number, string, list, or even a function—is treated as an object in memory. Objects have types, attributes, and methods associated with them.

Variables in Python are essentially labels or references that point to these objects in memory. When you assign a value to a variable, you're not storing the value directly in the variable; instead, the variable holds a reference (like a memory address) to the object where the value is stored.

### Key Concepts:
- **Working Memory**: Python uses a heap memory to store objects. The variable (e.g., `username`) is stored in the stack and points to the object on the heap.
- **Assignment**: When you assign a new value to a variable, it doesn't modify the existing object; it creates a new object (if needed) and updates the variable's reference to point to this new object.
- **Garbage Collection**: Python has an automatic garbage collector that detects and frees up memory occupied by objects that are no longer referenced by any variables. This prevents memory leaks.

This behavior is central to understanding the difference between **immutable** and **mutable** data types.

### Code Example: Variable Assignment and References
Let's demonstrate with a simple example using the `id()` function, which returns the unique memory address (identity) of an object.

```python
# Initial assignment
username = "Alice"
print("Username:", username)
print("Memory address:", id(username))  # Outputs a unique ID, e.g., 140000123456

# Changing the value
username = "Bob"
print("Username:", username)
print("Memory address:", id(username))  # Outputs a different ID, e.g., 140000789012

# The old "Alice" object is no longer referenced and will be garbage collected.
```

**Description**: Here, when we change `username` from "Alice" to "Bob", a new string object "Bob" is created in memory, and `username` now points to it. The old "Alice" object loses its reference and is eventually deleted by the garbage collector.

## Immutable vs Mutable Data Types
The key difference between immutable and mutable types lies in whether the object's value can be changed after creation.

- **Immutable Types**: Once created, their value cannot be modified. Any operation that seems to change them actually creates a new object. This makes them safe for use as dictionary keys or in sets (since they have consistent hash values).
- **Mutable Types**: Their contents can be modified in place without creating a new object. This is efficient for large data structures but requires caution when passing them to functions or using them in collections.

When you "change" an immutable object, Python creates a new object and updates the reference. For mutable objects, changes happen directly to the existing object.

### Immutable Data Types in Python
These cannot be altered after creation:
- **Integer** (`int`): Whole numbers, e.g., 5, -3.
- **Floating-point numbers** (`float`): Decimals, e.g., 3.14.
- **Boolean** (`bool`): True or False.
- **Strings** (`str`): Text, e.g., "Hello".
- **Tuples** (`tuple`): Ordered, immutable collections, e.g., (1, 2, 3).
- **Frozen Set** (`frozenset`): Immutable version of sets, e.g., frozenset({1, 2}).
- **Bytes** (`bytes`): Immutable byte sequences, e.g., b'hello'.

### Code Example: Immutable Types
```python
# String (immutable)
text = "Hello"
print("Original:", text, "ID:", id(text))

# Attempt to "change" it (creates a new object)
text = text + " World"
print("Modified:", text, "ID:", id(text))  # Different ID

# Integer (immutable)
num = 10
print("Original:", num, "ID:", id(num))

num += 5  # Creates a new int object
print("Modified:", num, "ID:", id(num))  # Different ID
```

**Description**: Notice how the `id()` changes after modification, indicating a new object. The old value is garbage collected if unreferenced.

### Mutable Data Types in Python
These can be modified in place:
- **List** (`list`): Ordered, changeable collections, e.g., [1, 2, 3].
- **Set** (`set`): Unordered, unique items, e.g., {1, 2, 3}.
- **Dictionary** (`dict`): Key-value pairs, e.g., {'key': 'value'}.
- **Bytearray** (`bytearray`): Mutable byte sequences, e.g., bytearray(b'hello').
- **Array** (from `array` module): Mutable arrays for efficient storage of basic types, e.g., array.array('i', [1, 2, 3]).

### Code Example: Mutable Types
```python
# List (mutable)
my_list = [1, 2, 3]
print("Original:", my_list, "ID:", id(my_list))

# Modify in place
my_list.append(4)
print("Modified:", my_list, "ID:", id(my_list))  # Same ID

# Dictionary (mutable)
my_dict = {'name': 'Alice'}
print("Original:", my_dict, "ID:", id(my_dict))

my_dict['age'] = 30  # Modify in place
print("Modified:", my_dict, "ID:", id(my_dict))  # Same ID
```

**Description**: The `id()` remains the same after changes, showing that the object itself was modified without creating a new one. No garbage collection occurs for the original object since it's still referenced.

## Key Differences in Practice
- **Immutable**: Safer for concurrency and hashing (e.g., as dict keys). Operations are less efficient for frequent changes (new objects created).
- **Mutable**: More efficient for modifications (no new objects). But beware of side effects, like when passing to functions—changes affect the original.

### Code Example: Mutable vs Immutable in Functions
```python
def modify_immutable(x):
    x += 1  # Creates a new int, doesn't affect original
    print("Inside function:", x)

def modify_mutable(lst):
    lst.append(4)  # Modifies the original list
    print("Inside function:", lst)

# Immutable
num = 10
modify_immutable(num)
print("After function:", num)  # Still 10

# Mutable
my_list = [1, 2, 3]
modify_mutable(my_list)
print("After function:", my_list)  # Now [1, 2, 3, 4]
```

**Description**: For immutable types, changes inside functions don't affect the original variable. For mutable, they do—because the reference points to the same object.

## Advanced Notes
- **Small Integers Caching**: Python caches small integers (-5 to 256) for efficiency, so their IDs might be the same even after reassignment.
- **String Interning**: Some strings are interned (shared references) for optimization.
- Use `is` operator to check if two variables point to the same object (identity), vs `==` for value equality.
- For custom classes, you can make them mutable or immutable by design.
