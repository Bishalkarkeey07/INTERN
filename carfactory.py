class Car:

    def __init__(self, car_type):
        self.car_type = car_type

    def get_description(self):
        return f"{self.car_type} car"
class SportsCar(Car):
    def __init__(self):
        super().__init__("Sports")

    def get_description(self):
        return super().get_description() + " with sporty features"


class SedanCar(Car):
    def __init__(self):
        super().__init__("Sedan")

    def get_description(self):
        return super().get_description() + " with comfortable features"


class SUV(Car):
    def __init__(self):
        super().__init__("SUV")

    def get_description(self):
        return super().get_description() + " with New  features"
 

class CarFactory:
    @staticmethod
    def create_car(car_type):
        if car_type == "sports":
            return SportsCar()
        elif car_type == "sedan":
            return SedanCar()
        elif car_type == "suv":
            return SUV()
        else:
            raise ValueError("No car avaliable")
car_factory = CarFactory()

car1 = input(car_factory.create_car)
print(car1.get_description())

car2 = input(car_factory.create_car)
print(car2.get_description())  

car3 =input(car_factory.create_car)
print(car3.get_description())  
