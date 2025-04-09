# Modular Arithmetic Formulas

# Modular Addition
# (a + b) % m = (a % m + b % m) % m

# Modular Subtraction
# (a - b) % m = ((a % m - b % m) + m) % m
# → We add + m to ensure the result is not negative.


# Modular Multiplication
# (a * b) % m = ((a % m) * (b % m)) % m


# Modular Division (using Fermat's Little Theorem)
# (a / b) % m = (a * b^(-1)) % m, where b^(-1) is the modular inverse of b mod m.
# → This is valid when m is prime. The modular inverse can be calculated using Fermat's Little Theorem:
# b^(-1) = b^(m-2) mod m


# Example usage of modular arithmetic formulas
# Note: In Python, the % operator automatically handles negative numbers correctly.

# Define values
a = 10
b = 15
m = 7

# 1. Modular Addition
add_result = (a % m + b % m) % m
print("Modular Addition:")
print(f"({a} + {b}) % {m} = {add_result}")  # Expected: (10 + 15) % 7 = 25 % 7 = 4

# 2. Modular Subtraction
sub_result = ((a % m - b % m) + m) % m
print("\nModular Subtraction:")
print(f"({a} - {b}) % {m} = {sub_result}")  # Expected: (10 - 15) % 7 = -5 % 7 = 2

# 3. Modular Multiplication
mul_result = (a % m * b % m) % m
print("\nModular Multiplication:")
print(f"({a} * {b}) % {m} = {mul_result}")  # Expected: (10 * 15) % 7 = 150 % 7 = 3



# 4. Modular Division using Fermat's Little Theorem (m must be prime)
a = 4
b = 3
m = 7
b_inv = pow(b, m - 2, m)  # Modular inverse of b mod m
div_result = (a * b_inv) % m
print("\nModular Division:")
print(f"({a} / {b}) % {m} = ({a} * {b_inv}) % {m} = {div_result}")
# 3^5 % 7 = 243 % 7 = 5, so (4 * 5) % 7 = 20 % 7 = 6
