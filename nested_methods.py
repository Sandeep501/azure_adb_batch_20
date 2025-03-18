# nested methods

# def outer_func():
#     def inner_func():
#         return "I'm an inner function!"
#     print(inner_func())
#     return "I'm an outer function!!"

def outer_func():
    def inner_func1():
        def inner_func2():
            return "I'm an inner function 2!"

        print(inner_func2())
        return "I'm an inner function 1!"

    print(inner_func1())
    return "I'm an outer function!!"




# print(outer_func())
print(inner_func1())