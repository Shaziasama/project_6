# Base class
class Person:
    def __init__(self, name):
        self.name = name

# Derived class
class Teacher(Person):
    def __init__(self, name, subject):
        super().__init__(name)  # Call base class constructor
        self.subject = subject
# Creating a Teacher object
teacher1 = Teacher("Shazia", "Mathematics")

# Accessing attributes
print("Name:", teacher1.name)
print("Subject:", teacher1.subject)
