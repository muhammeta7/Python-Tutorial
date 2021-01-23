# An expression is anything that can be calculated to return a value
# Value 12 is assigned/bound to variable a
a = 12
b = 3
print(a + b)    # 15
print(a - b)    # 9
print(a * b)    # 36
print(a / b)    # 4.0
print(a // b)    # 4
print(a % b)    # 0
print(a ** b)    # 1728

# Shorthand
for i in range(1, a//b):
    print(i) # i is expression because it needs to be evaluated
# Expressions 1 evaluates to 1, a//b evaluates to 4, range(1, a//b) needs to be evaluated to get 4.
# Can't have an expression bound to a value on the left of an assignment

# LongHand
i = 1
print(i)
i = 2
print(i)
i = 3
print(i)


