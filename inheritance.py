# Parent Class / Base Class
# child Class / inherited Class


# Parent Class
# class Animal:
#     def speak(self):
#         return "Animal Speaks"
    
#     def get_details(self):
#         return "This is an Animal class"

# # Child Class    
# class Dog(Animal):
#     def speak(self):
#         return "Dog Barks"
    
# dog_cls_inst = Dog()
# print(dog_cls_inst.speak())
# print(dog_cls_inst.get_details())


# Multiple Inheritence

class parent1:
    def function(self):
        return "Function from parent-1"
    
class parent2:
    def function(self):
        return "Function from parent-2"
    
class child(parent1, parent2):
    pass

obj = child()
print(obj.function())
# print(obj.function2())

# 3. Multi-level inheritance

class GrandParent():
    def grandParentMethod(self):
        return "I'm the grand parent"
    
class Parent(GrandParent):
    def parentMethod(self):
        return "I'm the Parent"

class Child(GrandParent):
    def childMethod(self):
        return "I'm the child method"

obj = Child()
# print(obj.childMethod())
# print(obj.grandParentMethod())
# print(obj.parentMethod)

