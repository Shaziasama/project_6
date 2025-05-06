# Engine class
class Engine:
    def start(self):
        return "Engine has started."

# Car class using composition
class Car:
    def __init__(self, engine):
        self.engine = engine  # Composed Engine object

    def start_car(self):
        return self.engine.start()  # Access Engine's method
# Creating an Engine object
my_engine = Engine()

# Passing Engine to Car
my_car = Car(my_engine)

# Starting the car (which starts the engine)
print(my_car.start_car())
