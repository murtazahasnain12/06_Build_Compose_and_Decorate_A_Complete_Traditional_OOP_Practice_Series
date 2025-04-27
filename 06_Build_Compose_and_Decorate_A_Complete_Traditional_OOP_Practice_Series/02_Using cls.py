class Counter:
    # Class variable to keep track of the count
    count = 0

    def __init__(self):
        # Increment the count whenever a new object is created
        Counter.count += 1

    @classmethod
    def show_count(cls):
        # Class method to display the count
        print(f"Total objects created: {cls.count}")


# Example usage
obj1 = Counter()
obj2 = Counter()
obj3 = Counter()

Counter.show_count()  # Output: Total objects created: 3
