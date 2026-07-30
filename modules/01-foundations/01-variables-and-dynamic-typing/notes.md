# Variables & Dynamic Typing

## What a variable actually is

In Python, a variable is a **name bound to an object**, not a labeled box
of memory. `x = 5` doesn't put `5` inside a box called `x` — it creates the
integer object `5` somewhere in memory and makes the name `x` point to it.

```python
x = 5
y = x      # y points to the SAME object as x, not a copy
```

You can see this with `id()`, which returns an object's memory address, and
`is`, which checks whether two names point to the *same* object (as
opposed to `==`, which checks equal *value*):

```python
x = 5
y = x
print(id(x) == id(y))   # True — same object
print(x is y)            # True
print(x == y)            # True — same value too
```

Small integers (-5 to 256) and short strings are **cached/interned** by
CPython, so `is` can look "true" for equal small ints even without
assignment linking them. Never rely on `is` for value comparison — use
`==`. Reserve `is` for identity checks like `x is None`.

## Dynamic typing

Python is **dynamically typed**: a name isn't declared with a fixed type —
it can be rebound to a value of any type at any time.

```python
x = 5        # x refers to an int
x = "hello"  # now x refers to a str — perfectly legal
```

This is different from **static typing** (Java, C, Rust), where a variable
has a fixed type declared up front and the compiler enforces it. Python
checks types **at runtime**, not compile time — this is what "dynamic"
means. The *object* always knows its own type (`type(x)`); it's the *name*
that's flexible.

Python is also **strongly typed**: it won't silently coerce incompatible
types for you.

```python
"3" + 3      # TypeError — Python won't guess you meant "33" or 6
```

Compare to JavaScript, which is dynamically *and weakly* typed and would
happily coerce `"3" + 3` to `"33"`. Strong typing is one reason Python
errors are more predictable to debug.

## Naming rules and conventions

**Rules (enforced by the interpreter):**
- Must start with a letter or underscore, followed by letters, digits, underscores.
- Case-sensitive (`age` and `Age` are different names).
- Cannot be a reserved keyword (`class`, `if`, `for`, `import`, ...).

**Conventions (enforced by convention/linters, e.g. PEP 8 — not the interpreter):**
- `snake_case` for variables and functions: `user_age`, `total_count`.
- `UPPER_SNAKE_CASE` for constants: `MAX_RETRIES = 3`.
- `PascalCase` for classes (covered in Module 04).
- Leading underscore `_name` signals "internal use" by convention only —
  Python does not enforce privacy.
- Avoid single-letter names except in short-lived contexts (loop counters,
  math formulas).

## Multiple assignment & unpacking

```python
a, b, c = 1, 2, 3          # tuple unpacking
a = b = c = 0              # all three names bound to the same object
first, *rest = [1, 2, 3, 4]  # first = 1, rest = [2, 3, 4]
```

## `type()` and checking what you have

```python
type(5)          # <class 'int'>
type("hi")       # <class 'str'>
type(3.14)       # <class 'float'>
type(None)       # <class 'NoneType'>
isinstance(5, int)  # True — prefer this over type() == for checks
```

`isinstance()` is generally preferred over comparing `type(x) == int`
because it also respects inheritance (relevant once we hit Module 04).

## Key takeaway

A variable name is a reference, not a container. Reassigning a name never
mutates the object it used to point to — it just points the name
somewhere else. This distinction matters a lot once we get to mutable vs.
immutable objects (Module 03).
