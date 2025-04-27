class Engine:
    def start(self):
        print("Engine has started.")

class Car:
    def __init__(self, engine):
        self.engine = engine  # Composition: Car *has an* Engine

    def start_car(self):
        self.engine.start()  # Accessing Engine's method

# Example usage
my_engine = Engine()
my_car = Car(my_engine)

my_car.start_car()
