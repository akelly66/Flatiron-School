class ShoppingCart:
    # write your code here
    def __init__(self, total = 0, employee_discount=None, items= []):
        self.total = total
        self.emp_discount = employee_discount
        self.items = items
    def add_item(self, name, price, quantity=1):
       pass
    def mean_item_price(self):
       pass

    def median_item_price(self):
        pass

    def apply_discount(self):
       pass

    def void_last_item(self):
        pass