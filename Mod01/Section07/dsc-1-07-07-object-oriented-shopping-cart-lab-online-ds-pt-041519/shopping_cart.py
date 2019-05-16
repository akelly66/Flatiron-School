class ShoppingCart:
    # write your code here
    def __init__(self, total = 0, employee_discount=None, items= []):
        self.items = items
        self.total = total
        self.employee_discount = employee_discount
        
    def add_item(self, name, price, quantity=1):
        self.items.append({'name': name, 'price': price, 'quantity': quantity})   
        self.total += price*quantity
        return self.total
    def mean_item_price(self):
        return self.total/(sum(item['quantity'] for item in self.items))
    
    def median_item_price(self):
        prices = list(item['price'] for item in self.items)
        prices.sort()
        if len(prices)%2==0:
            val1_index = int((len(prices) / 2) - 1)
            val2_index = val1_index + 1
            return (prices[val1_index] + prices[val2_index]) / 2
        else:
            med_index = (len(prices) // 2) 
            return prices[med_index]
        
    def apply_discount(self):
        if self.employee_discount:
            discount = self.employee_discount/100
            total_with_discount = self.total-(self.total*discount)
            return total_with_discount
        else:
            print("Sorry, there is no discount for you today. :(")

    def void_last_item(self):
        if self.items:
            removed_item = self.items.pop()   
        else:
            return "You have no more items!"
        self.total -= removed_item['price']