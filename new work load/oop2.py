# using oop, create a class called class that has the following attributes; model, color, year of manfctr.
#implement constructor method and a method function that prints , my favorite car is that model, this color, and was mnfctrd in -years
#create 5 instances of that class

class Cars:
    def __init__(self, color, model,year):
        self.color = color
        self.model = model
        self.year = year

    def describe(self):
        print(f"Hello, I am YMO. The car of my dreams is a {self.color} {self.model}, a classic of the year {self.year} ")

car1 = Cars("Blue", "Ford", 1995)
car1.describe()

car2 = Cars("Black", "Mustang", 1999)
car2.describe()

car3 = Cars("Red", "Toyota", 1979)
car3.describe()

car4= Cars("Orange", "Honda", 2004)
car4.describe()

car5 = Cars("Dark Purple", "Lamborgini", 2019)
car5.describe()