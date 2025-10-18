# create an a class caled "Car"

class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        return f'{self.make} {self.model} {self.year}'
        
    pass

# instance of object "Car"
car1 = Car("Toyota", "Camry", 2020)
car2 = Car("Citroen", "C3", 2011)

print(car1.display_info())
print(car2.display_info())

# Inheritence and polimorphism
class EletricCar(Car):
    def __init__(self, make, model, year, battery_capacity):
        super().__init__(make, model, year)
        self.battery_capacity = battery_capacity

    def display_info(self):
        return f'{self.make} {self.model} {self.year} with {self.battery_capacity} KWh battery.'
    
car3 = EletricCar("Volvo", "XC90", 2025, 40000)

print(car3.display_info())
