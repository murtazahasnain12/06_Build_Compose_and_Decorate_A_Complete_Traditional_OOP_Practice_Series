class Employee:
    def __init__(self, name, salary, ssn):
        self.name = name           # Public variable
        self._salary = salary      # Protected variable
        self.__ssn = ssn           # Private variable

# Creating an object of Employee
emp = Employee("Alice", 75000, "123-45-6789")

# Accessing variables
print("Public:", emp.name)         # ✅ This works

print("Protected:", emp._salary)   # ⚠️ This works, but not recommended by convention

try:
    print("Private:", emp.__ssn)   # ❌ This will raise an AttributeError
except AttributeError as e:
    print("Private:", e)

# Accessing private variable using name mangling
print("Private (via name mangling):", emp._Employee__ssn)  # ✅ This works
