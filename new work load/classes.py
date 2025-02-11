#object oriented programming
class Person:
    def __init__(self, name, age):
        # this is a constructor method, it takes two parameters and initializes as attributes.
        self.name = name
        self.age = age

    def myfunction(self):
        print(f"Hello, my name is  {self.name} and I am {self.age} years old.")
        # this is a method function
# create an object or an instance of a class
my_object = Person("Yahya Mohamed", 17)
my_object.myfunction()

my_object2=Person("John Doe", 21)
my_object2.myfunction()

objective = Person("John Slow", 121)
objective.myfunction()

objective1 = Person("John Snow", 211)
objective1.myfunction()

objective2 = Person("John Throw", 221)
objective2.myfunction()
