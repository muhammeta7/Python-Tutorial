# Expression is combination of values, variables, and operators.
# Value 12 is assigned/bound to variable a
# A value or a variable by itself is considered an expression
# A statement is a unit of code that has an effect, like creating a variable or displaying a value.

a = 12
b = 3
print(a + b)  # 15
print(a - b)  # 9
print(a * b)  # 36
print(a / b)  # 4.0
print(a // b)  # 4
print(a % b)  # 0
print(a ** b)  # 1728

# -------------------------------------------------------------------------

# Operator Precedence / Order of Operations
print(a + b / 3 - 4 * 12)  # -35.0
print(a + (b / 3) - (4 * 12))  # 35.0
print((((a + b) / 3) - 4) * 12)  # 12.0
print(((a + b) / 3 - 4) * 12)
#  Do not be afraid to break it up into smaller parts
c = a + b
d = c / 3
e = d - 4
print(e * 12)

# Examples with mixed operations of equal precedence
print(a / (b * a) / b)  # 0.11111111111
