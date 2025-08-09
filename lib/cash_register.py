class CashRegister:
    def __init__(self, discount=0):
        self.discount = discount
        self.total = 0
        self.items = []
        self.last_transaction_amount = 0

    def add_item(self, title, price, quantity=1):
        transaction_amount = price * quantity
        self.total += transaction_amount
        self.items.extend([title] * quantity)
        self.last_transaction_amount = transaction_amount  # store last added item's total value

    def apply_discount(self):
        if self.discount > 0:
            self.total = self.total * (100 - self.discount) / 100
            print(f"After the discount, the total comes to ${self.total:.0f}.")
        else:
            print("There is no discount to apply.")
        
    def void_last_transaction(self):
        self.total -= self.last_transaction_amount
