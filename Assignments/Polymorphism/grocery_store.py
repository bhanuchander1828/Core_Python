"""
ITMD 513 : Assignment- Polymorphism - Bhanu kureti
Summary : This program will create Grocery store class with attributes total revenue, grocery store type
and inherits all attributes and methods of store class
"""
# Import Store class from Store,py program
from Store import Store


# define GroceryStore class
class GroceryStore(Store):

    # constructor
    def __init__(self, s_name, s_address, s_status, s_sales_tax_percentage, g_store_type):
        super().__init__(s_name, s_address, s_status, s_sales_tax_percentage)
        self.total_revenue = 0
        self.g_store_type = g_store_type

    # function that takes the quantity and price of item to sell as input and returns the total revenue after selling
    def sell_item(self, quantity, price_item):
        self.total_revenue += float(quantity) * price_item
        return self.total_revenue  # return the updated total_revenue

    # mutator of grocery store class
    def set_g_store_type(self, g_store_type):
        self.g_store_type = g_store_type

    # accessor of grocery store class
    def get_store_type(self):
        return self.store_type

    # calculate and return total sales revenue
    def calculate_total_sales(self):
        return float(self.total_revenue)

    # calculate and return total sales tax
    def calculate_total_sales_tax(self):
        return float(self.total_revenue * self.get_s_sales_tax_percentage()) / 100


