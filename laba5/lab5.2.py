class Circle:
    def __init__(self, radius):
        self.radius = radius


    def get_radius(self):
        return self.radius


    def set_radius(self, new_radius=input()):
        self.radius = new_radius



Circle = Circle(6)
print('Радиус круга:', Circle.get_radius())
Circle.set_radius()
print('Новый радиус круга:', Circle.get_radius())
