# Step 1: Create a custom exception
class InvalidAgeError(Exception):
    pass

# Step 2: Define a function that uses it
def check_age(age):
    if age < 18:
        raise InvalidAgeError("Age must be at least 18.")

# Step 3: Handle it with try...except
try:
    user_age = int(input("Enter your age: "))
    check_age(user_age)
    print("Access granted!")
except InvalidAgeError as e:
    print(f"Access denied: {e}")
