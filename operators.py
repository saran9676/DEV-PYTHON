# Arithmetic Operators
a, b = 10, 5
addition = a + b
subtraction = a - b
multiplication = a * b
division = a / b
remainder = a % b
exponentiation = a ** b
floor_division = a // b

# Comparison Operators
equal = a == b
not_equal = a != b
greater_than = a > b
less_than = a < b
greater_than_or_equal = a >= b
less_than_or_equal = a <= b

# Logical Operators
logical_and = (a > 0) and (b > 0)
logical_or = (a > 0) or (b > 0)
logical_not = not (a > 0)

# Assignment Operators
c = a  # simple assignment
c += b  # c = c + b
c -= b  # c = c - b
c *= b  # c = c * b
c /= b  # c = c / b
c %= b  # c = c % b
c **= b  # c = c ** b
c //= b  # c = c // b

# Bitwise Operators
bitwise_and = a & b
bitwise_or = a | b
bitwise_xor = a ^ b
bitwise_not_a = ~a
left_shift = a << 1
right_shift = a >> 1

# Membership Operators
list_example = [1, 2, 3, 4, 5]
membership_in = 3 in list_example
membership_not_in = 6 not in list_example

# Print Results
print("Arithmetic Operators:")
print(f"Addition: {addition}")
print(f"Subtraction: {subtraction}")
print(f"Multiplication: {multiplication}")
print(f"Division: {division}")
print(f"Remainder: {remainder}")
print(f"Exponentiation: {exponentiation}")
print(f"Floor Division: {floor_division}")

print("\nComparison Operators:")
print(f"Equal: {equal}")
print(f"Not Equal: {not_equal}")
print(f"Greater Than: {greater_than}")
print(f"Less Than: {less_than}")
print(f"Greater Than or Equal: {greater_than_or_equal}")
print(f"Less Than or Equal: {less_than_or_equal}")

print("\nLogical Operators:")
print(f"Logical AND: {logical_and}")
print(f"Logical OR: {logical_or}")
print(f"Logical NOT: {logical_not}")

print("\nAssignment Operators:")
print(f"Simple Assignment: {c}")
print(f"Add and Assign: {c}")
print(f"Subtract and Assign: {c}")
print(f"Multiply and Assign: {c}")
print(f"Divide and Assign: {c}")
print(f"Modulo and Assign: {c}")
print(f"Exponentiate and Assign: {c}")
print(f"Floor Divide and Assign: {c}")

print("\nBitwise Operators:")
print(f"Bitwise AND: {bitwise_and}")
print(f"Bitwise OR: {bitwise_or}")
print(f"Bitwise XOR: {bitwise_xor}")
print(f"Bitwise NOT (a): {bitwise_not_a}")
print(f"Left Shift: {left_shift}")
print(f"Right Shift: {right_shift}")

print("\nMembership Operators:")
print(f"Membership IN: {membership_in}")
print(f"Membership NOT IN: {membership_not_in}")


'''outputs:
Arithmetic Operators:
------------------------
Addition: 15
Subtraction: 5
Multiplication: 50
Division: 2.0
Remainder: 0
Exponentiation: 100000
Floor Division: 2

Comparison Operators:
------------------------
Equal: False
Not Equal: True
Greater Than: True
Less Than: False
Greater Than or Equal: True
Less Than or Equal: False

Logical Operators:
----------------------
Logical AND: True
Logical OR: True
Logical NOT: False

Assignment Operators:
---------------------------
Simple Assignment: 0.0
Add and Assign: 0.0
Subtract and Assign: 0.0
Multiply and Assign: 0.0
Divide and Assign: 0.0
Modulo and Assign: 0.0
Exponentiate and Assign: 0.0
Floor Divide and Assign: 0.0

Bitwise Operators:
-------------------------
Bitwise AND: 0
Bitwise OR: 15
Bitwise XOR: 15
Bitwise NOT (a): -11
Left Shift: 20
Right Shift: 5

Membership Operators:
------------------------------
Membership IN: True
Membership NOT IN: True'''
