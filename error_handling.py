a = int(input("a: "))
b = int(input("b: "))

def division(num1, num2):
    # error handling
    try:
        r = num1 // num2
    except Exception as e:
        r = e
    finally:
        print("Program completed!")
    return r

def addition(num1, num2):
    return num1 + num2

print(division(a, b))
print(addition(a, b))