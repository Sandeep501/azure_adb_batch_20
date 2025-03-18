# Class syntax

class Car:
    
    dummy_var = "my_var"
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        self.speed = 0
    
    def accelerate(self, amount):
        self.speed += amount
        return f"Accelrating... New speed: {self.speed} km/hr"

    def breake(self, amount):
        self.speed = max(0, self.speed - amount)
        return f"Braking... New speed: {self.speed} km/hr"
    
    def display_info(self):
        return f"{self.brand}, {self.model}, {self.year}"


bmw_instance = Car("BMW", "XL7", "2025")
print(bmw_instance.display_info())
print(bmw_instance.accelerate(100))
print(bmw_instance.breake(90))
print(bmw_instance.dummy_var)
