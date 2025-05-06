class Multiplier:
    def __init__(self, factor):
        self.factor = factor

    def __call__(self, number):
        return number * self.factor
# Create a Multiplier object with a factor of 3
triple = Multiplier(3)

# Check if object is callable
print("Is 'triple' callable?", callable(triple))

# Use the object like a function
result = triple(10)
print("Result of triple(10):", result)
