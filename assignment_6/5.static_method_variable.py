#Create a class MathUtils with a static method add(a, b) that returns the sum. No class or instance variables should be used.

class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b
# Calling the static method directly using the class name
result = MathUtils.add(10, 20)
print("Sum:", result)
