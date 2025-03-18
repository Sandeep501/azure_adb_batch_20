a = int(input("Enter a value: "))
b = int(input("Enter b value: "))
func = input("Choose the function: ")

def addition(a, b):
    return a + b

def sub(a, b):
    return a - b

def multiply(a, b):
    return a * b

def division(a, b):
    return a//b

def main(a, b, func='a'):
    if func == 'a':
        return addition(a, b)
    elif func == 's':
        return sub(a, b)
    elif func == 'm':
        return multiply(a, b)
    elif func == 'd':
        return division(a, b)
    else:
        raise "Please enter valid func code!"
    
print(main(a, b, func))