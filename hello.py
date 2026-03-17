# import utils  # This will compile utils.py to utils.cpython-312.pyc in __pycache__

# print(utils.multiply(2, 3))  # Output: 6
def fibonacci_generator(limit):
    a, b = 0, 1
    while a < limit:
        yield a  # Yield the next number
        a, b = b, a + b  # Update for next iteration

# Using the generator
fib_gen = fibonacci_generator(10)

print(fib_gen)  # Output: 0 1 1 2 3 5 8

# Generators can be converted to lists if needed
print(list(fibonacci_generator(10)))  # Output: [0, 1, 1, 2, 3, 5, 8]
# python ke baad fastapi krna