#Create a class Car with a public variable brand and a public method start(). Instantiate the class and access both from outside the class.
class Car:
    def __init__(self, brand):
        self.brand = brand  # Public variable

    def start(self):
        print(f"The {self.brand} car has started.")
# Creating an object of Car
my_car = Car("Toyota")

# Accessing public variable
print("Car Brand:", my_car.brand)

# Calling public method
my_car.start()

