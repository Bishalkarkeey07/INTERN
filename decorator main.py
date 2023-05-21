# Project Description:
# Create a race car game where players can choose a car, customize it,
# and race against other cars on different tracks. 
# The game should follow the SOLID principle and
# implement the factory design pattern to create different types of cars. 
# Additionally, threading should be used to ensure that the game runs smoothly.

    # Task Breakdown:
# 1..Create a Car class that implements the decorator pattern to 
# add customizations such as paint jobs, spoilers, and rims to the car.

# 2..Implement a CarFactory class that creates different types of cars such as sports cars, sedans, and SUVs.


class Car:
    def __init__(self):
        self.description = "The Basic cars :"

    def get_description(self):
        return self.description
    
class CarDecorator(Car):
    def __init__(self, car):
        self.car = car

    def get_description(self):
        return self.car.get_description()


class PaintJobDecorator(CarDecorator):  #multilevel ingeritance is used.
    def __init__(self, car, paint_color):
        super().__init__(car)
        self.paint_color = paint_color


    def get_description(self):
        return self.car.get_description() + f", {self.paint_color} paint job"


class SpoilerDecorator(CarDecorator):
    def __init__(self, car):
        super().__init__(car)

    def get_description(self):
        return self.car.get_description() + ", spoiler"


class RimsDecorator(CarDecorator):
    def __init__(self, car):
        super().__init__(car)

    def get_description(self):
        return self.car.get_description() + ", rims"

basic_car = Car()
print(basic_car.get_description())  

# Adding customizations

