"""Solved version of modules/01-foundations/01-variables-and-dynamic-typing/practice.py"""

# TODO 1
my_name = "Sarthak"
my_age = 25

assert isinstance(my_name, str), "my_name should be a string"
assert isinstance(my_age, int), "my_age should be an int"


# TODO 2
mystery_types = []
mystery = 123
mystery_types.append(type(mystery))
mystery = "now a string"
mystery_types.append(type(mystery))
mystery = [1, 2, 3]
mystery_types.append(type(mystery))

assert mystery_types == [int, str, list], f"got {mystery_types}"


# TODO 3
red = green = blue = 0

assert red == 0 and green == 0 and blue == 0
assert red is green is blue, "all three should be the SAME object"


# TODO 4
numbers = [5, 10, 15, 20, 25]
head, *tail = numbers

assert head == 5
assert tail == [10, 15, 20, 25]


# TODO 5
quantity = 7
label = "Quantity: "
message = label + str(quantity)

assert message == "Quantity: 7", f"got {message!r}"


# TODO 6
is_valid = True
bool_is_int_subclass = isinstance(is_valid, int)

assert bool_is_int_subclass is True


print("All checks passed!")
