class Bank:
    # Class variable
    bank_name = "Default Bank"

    def __init__(self, account_holder):
        self.account_holder = account_holder

    @classmethod
    def change_bank_name(cls, name):
        cls.bank_name = name

    def display(self):
        print(f"Account Holder: {self.account_holder}")
        print(f"Bank Name: {self.bank_name}")


# Creating instances
account1 = Bank("Alice")
account2 = Bank("Bob")

# Displaying initial bank names
print("Before changing bank name:")
account1.display()
account2.display()

# Changing bank name using class method
Bank.change_bank_name("NextGen Bank")

# Displaying after changing the bank name
print("\nAfter changing bank name:")
account1.display()
account2.display()
