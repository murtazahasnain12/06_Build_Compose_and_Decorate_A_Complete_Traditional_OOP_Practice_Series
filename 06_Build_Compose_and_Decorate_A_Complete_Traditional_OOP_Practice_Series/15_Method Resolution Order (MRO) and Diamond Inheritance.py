# Class A
class A:
    def show(self):
        print("Show from class A")

# Class B inherits from A
class B(A):
    def show(self):
        print("Show from class B")

# Class C inherits from A
class C(A):
    def show(self):
        print("Show from class C")

# Class D inherits from B and C
class D(B, C):
    pass

# Create object of class D
d = D()

# Call show() method
d.show()

# Print the Method Resolution Order
print(D.mro())
