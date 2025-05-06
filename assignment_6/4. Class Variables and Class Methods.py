class Bank:
    bank_name = "ABC Bank"  # Class variable

    def __init__(self, customer_name):
        self.customer_name = customer_name

    @classmethod
    def change_bank_name(cls, name):
        cls.bank_name = name
# Creating instances
customer1 = Bank("Shazia")
customer2 = Bank("Zohaib")

# Accessing the class variable through instances
print("Before change:")
print(customer1.customer_name, "-", customer1.bank_name)
print(customer2.customer_name, "-", customer2.bank_name)

# Changing the bank name using class method
Bank.change_bank_name("XYZ Bank")

# Accessing again to see the change reflected
print("\nAfter change:")
print(customer1.customer_name, "-", customer1.bank_name)
print(customer2.customer_name, "-", customer2.bank_name)
