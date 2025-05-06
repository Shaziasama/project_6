#. Constructors and Destructors
#Create a class Logger that prints a message when an object is created (constructor) and another message when it is destroyed (destructor).
class Logger:
    def __init__(self):
        print("Logger object has been created.")

    def __del__(self):
        print("Logger object has been destroyed.")
# Creating and deleting the object
logger1 = Logger()

# Optionally force destruction
del logger1

