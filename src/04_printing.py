"""
Python provides a number of ways to perform printing. Research
how to print using the printf operator, the `format` string 
method, and by using f-strings.
"""

x = 10
y = 2.24552
z = "I like turtles!"

# Using the printf operator (%), print the following feeding in the values of x,
# y, and z:
# x is 10, y is 2.25, z is "I like turtles!"
print(y)
print(z)

# Use the 'format' string method to print the same thing
txt = "x is {x:.2f}"
print(txt.format(x = 10))

txt = "y is {y:.2f}"
print(txt.format(y = 2.25))

# txt = "z is {z:.2f}"
# print(txt.format(z = "I like turtles!"))
# Finally, print the same thing using an f-string

x = 10
print(f"x = {x}")

y = 2.25
print(f"y = {y}")

z = "I like turtles!"
print(f"z = {z}")