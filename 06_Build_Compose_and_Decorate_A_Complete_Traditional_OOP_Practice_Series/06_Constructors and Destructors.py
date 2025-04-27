class Logger:
    def __init__(self):
        print("Logger object has been created.")

    def __del__(self):
        print("Logger object has been destroyed.")

# Example usage:
logger = Logger()

# You can force destruction (though not recommended) using:
# del logger
