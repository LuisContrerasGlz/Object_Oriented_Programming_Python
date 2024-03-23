class Item:
    pay_rate = 0.8 # The Pay rate after 20% discount 
    all = [] 

    def __init__(self, name: str, price: float, quantity = 0):
        # Run validations to the recieved arguments
        assert price >= 0, f"Price {price} is not greater or equal to Zero"
        assert quantity >= 0,  f"quantity {quantity} is not greater or equal to Zero"

        # Assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity

        # Actions to execute
        Item.all.append(self)
    
    def calculate_total_price(self):
        return self.price * self.quantity
    
    def apply_discount(self):
        self.price = self.price * self.pay_rate

    def __repr__(self):
        return f"Item('{self.name}', {self.price}, {self.quantity})"
    
item1 = Item("Phone", 100, 2)
item2 = Item("Laptoo", 200, 2)

print(item1.calculate_total_price())
print(item2.calculate_total_price())

item1.apply_discount()
print(item1.price())

item3 = Item("Cable", 10, 5)
item4 = Item("Mouse", 50, 5)
item5 = Item("Keyboard", 75, 5)

print(Item.all)


