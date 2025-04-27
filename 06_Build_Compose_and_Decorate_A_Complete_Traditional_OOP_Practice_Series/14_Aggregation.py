# Define the Employee class
class Employee:
    def __init__(self, name, emp_id):
        self.name = name
        self.emp_id = emp_id

    def display(self):
        print(f"Employee ID: {self.emp_id}, Name: {self.name}")

# Define the Department class
class Department:
    def __init__(self, dept_name, employee):
        self.dept_name = dept_name
        self.employee = employee  # Aggregation: Department has an Employee

    def show_details(self):
        print(f"Department: {self.dept_name}")
        self.employee.display()

# Create an Employee object (independent)
emp1 = Employee("Alice Johnson", 101)

# Create a Department object and pass the Employee object to it
dept1 = Department("Human Resources", emp1)

# Display information
dept1.show_details()

# Notice that emp1 exists independently of dept1
print("\nAccessing employee separately:")
emp1.display()
