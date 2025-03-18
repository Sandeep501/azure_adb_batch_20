# function or methods

def function_name():
    return "Hello World!!"

print(function_name())

def addition(a, b):
    return a + b

print(addition(10, 30))
print(addition(a=100, b=30))

# default parameter values
def multiply(a, b=2):
    return a * b

print(multiply(a=20, b=3))

def multiply_three_digit(a, c, b=2):
    return (a * b) + c

print(multiply_three_digit(a=2, b=10, c=20))
