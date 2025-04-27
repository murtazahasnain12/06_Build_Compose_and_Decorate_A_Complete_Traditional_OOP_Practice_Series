# Define the decorator
def log_function_call(func):
    def wrapper():
        print("Function is being called")
        func()
    return wrapper

# Define a function and apply the decorator
@log_function_call
def say_hello():
    print("Hello!")

# Call the function
say_hello()
