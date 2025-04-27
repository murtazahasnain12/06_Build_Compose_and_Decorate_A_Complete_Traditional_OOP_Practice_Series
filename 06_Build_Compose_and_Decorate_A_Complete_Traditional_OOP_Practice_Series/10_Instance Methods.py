class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        print(f"{self.name} says: Woof!")

# Example of creating a Dog and calling bark
my_dog = Dog("Buddy", "Golden Retriever")
my_dog.bark()
