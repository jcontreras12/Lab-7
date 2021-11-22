# Jose Contreras
# Date 11/13/21
# problem 6 is creating a class car

class car:
    def __init__(self, model, year, color, manufacturer, type):
        self.model = model
        self.year = year
        self.color = color
        self.manufacturer = manufacturer
        self.type = type

    def get_model(self):
        return self.model

    def get_year(self):
        return self.year

    def get_color(self):
        return self.color

    def get_manufacturer(self):
        return self.manufacturer

    def get_type(self):
        return self.type


    def fullspecs(self):
        return self.model + ' ' + str(self.year) + ' ' + self.color + ' ' + self.manufacturer + ' ' + self.type + ''

car1 = car("Sports", 2012, "Blue", "limited edition", "honda")
car2 = car("Sedan", 2020, "Black", "limited", "toyota")

print(car1.get_color())
print(car1.get_model())
print(car1.fullspecs())
print(car2.get_color())
print(car2.fullspecs())