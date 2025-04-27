class Multiplier:
    def __init__(self, factor):
        self.factor = factor

    def __call__(self, number):
        return number * self.factor

# Create an instance
double = Multiplier(2)

# Test if the object is callable
print(callable(double))  # Should print True

# Call the object like a function
result = double(10)  # Should return 20
print(result)
