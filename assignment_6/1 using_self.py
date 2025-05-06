class Student:
    def __init__(self, name, marks):
        self.name = name      # Initialize name
        self.marks = marks    # Initialize marks

    def display(self):
        print(f"Student Name: {self.name}")
        print(f"Marks: {self.marks}")


        # Creating an object of Student
student1 = Student("Shazia", 85)

# Displaying student details
student1.display()

