class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model


    def get_info(self):
        return f'Care make: {self.make}, model: {self.model}'


class Car(Vehicle):
    def __init__(self, make, model, fuel_type):
        super().__init__(make, model)
        self.fuel_type = fuel_type


    def get_info(self):
        return f'Care make: {self.make}, model: {self.model}, fuel type: {self.fuel_type}'

make = 'Ford'
model = 'Focus'
vehicle = Vehicle(make, model)
print(vehicle.get_info())

car = Car(make, model, 'Бензин')
print(car.get_info())