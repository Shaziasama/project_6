
# Employee class (independent)
class Employee:
    def __init__(self, name, emp_id):
        self.name = name
        self.emp_id = emp_id

    def get_details(self):
        return f"Employee ID: {self.emp_id}, Name: {self.name}"

# Department class (aggregates Employee)
class Department:
    def __init__(self, dept_name, employee):
        self.dept_name = dept_name
        self.employee = employee  # Reference to an existing Employee object

    def show_department_info(self):
        print(f"Department: {self.dept_name}")
        print("Employee:", self.employee.get_details())
# Create an independent Employee object
emp1 = Employee("Shazia", 101)

# Pass it to a Department (aggregation)
dept1 = Department("HR", emp1)

# Display department info
dept1.show_department_info()
