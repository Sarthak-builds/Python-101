"""Worked demo: variables, naming, and dynamic typing."""

# --- A variable is a name bound to an object ---
x = 5
y = x
print(f"x = {x}, y = {y}")
print(f"x is y: {x is y}")   # same object -> True
print(f"id(x) == id(y): {id(x) == id(y)}")

# --- Dynamic typing: the same name can point to different types over time ---
value = 5
print(f"value = {value!r}, type = {type(value)}")
value = "now I'm a string"
print(f"value = {value!r}, type = {type(value)}")
value = [1, 2, 3]
print(f"value = {value!r}, type = {type(value)}")

# --- Strong typing: Python won't silently coerce incompatible types ---
try:
    result = "3" + 3
except TypeError as e:
    print(f"TypeError as expected: {e}")

# The correct, explicit ways to combine a string and a number:
print("3" + str(3))   # "33" — explicit string concatenation
print(int("3") + 3)   # 6   — explicit numeric addition

# --- Multiple assignment & unpacking ---
a, b, c = 1, 2, 3
print(f"a={a}, b={b}, c={c}")

first, *rest = [10, 20, 30, 40]
print(f"first={first}, rest={rest}")

shared = other = 100
print(f"shared={shared}, other={other}, shared is other: {shared is other}")

# --- type() vs isinstance() ---
count = 42
print(f"type(count) is int: {type(count) is int}")
print(f"isinstance(count, int): {isinstance(count, int)}")

# isinstance is preferred because it also respects inheritance —
# a bool is technically a subclass of int in Python:
is_active = True
print(f"isinstance(True, int): {isinstance(is_active, int)}")
