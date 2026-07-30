"""Practice: variables, naming, and dynamic typing.

Fill in each TODO. Run this file when you're done — the asserts will tell
you if something's wrong. Don't look at solutions/ until you've tried.
"""

# TODO 1: Assign your name (a string) to `my_name`, and your age (an int)
# to `my_age`.
my_name = ...
my_age = ...

assert isinstance(my_name, str), "my_name should be a string"
assert isinstance(my_age, int), "my_age should be an int"


# TODO 2: Reassign `mystery` to three different types, in order:
# an int, then a string, then a list. Store each `type(mystery)` result
# in `mystery_types` as you go, so it ends up with 3 items.
mystery_types = []
mystery = 123
mystery_types.append(type(mystery))
# TODO: reassign `mystery` to a string, append its type
# TODO: reassign `mystery` to a list, append its type

assert mystery_types == [int, str, list], f"got {mystery_types}"


# TODO 3: Using multiple assignment on ONE line, create three variables
# `red`, `green`, `blue` all bound to the integer 0.
...

assert red == 0 and green == 0 and blue == 0
assert red is green is blue, "all three should be the SAME object"


# TODO 4: Given the list below, use starred unpacking on ONE line to get
# the first element into `head` and everything else into `tail` (a list).
numbers = [5, 10, 15, 20, 25]
# head, *tail = ...

assert head == 5
assert tail == [10, 15, 20, 25]


# TODO 5: Fix the TypeError below WITHOUT changing the values of
# `quantity` or `label` — only change how they're combined — so that
# `message` becomes the string "Quantity: 7".
quantity = 7
label = "Quantity: "
message = ...  # should equal "Quantity: 7"

assert message == "Quantity: 7", f"got {message!r}"


# TODO 6: `is_valid` is a bool. Without changing its value, write an
# expression proving that bool is a subclass of int in Python — assign
# the boolean result of that check to `bool_is_int_subclass`.
is_valid = True
bool_is_int_subclass = ...

assert bool_is_int_subclass is True


print("All checks passed!")
