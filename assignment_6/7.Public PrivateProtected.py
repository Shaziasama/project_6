class Employee:
    def __init__(self, name, salary, ssn):
        self.name = name        # Public variable
        self._salary = salary   # Protected variable (by convention)
        self.__ssn = ssn        # Private variable (name mangling)
emp = Employee("Shazia", 50000, "123-45-6789")

# Access public variable
print("Name:", emp.name)

# Access protected variable (possible, but not recommended directly)
print("Salary (protected):", emp._salary)

# Access private variable (not directly accessible)
# print(emp.__ssn)  # This will raise an AttributeError

# Access private variable using name mangling
print("SSN (private):", emp._Employee__ssn)
