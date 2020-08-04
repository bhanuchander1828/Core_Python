"""
ITMD 513 : Assignment-Polymorphism - Bhanu kureti
Summary : This program will create Stores abstract class with attributes Name, Address, Status and Sales_tax_percent
"""


# Define abstract class store
class Store:

    # constructor
    def __init__(self, s_name, s_address, s_status, s_sales_tax_percentage):
        self.s_name = s_name
        self.s_address = s_address
        self.s_status = s_status
        self.s_sales_tax_percent = s_sales_tax_percentage

    # mutators of store class
    def set_s_name(self, s_name):
        self.s_name = s_name

    def set_s_address(self, s_address):
        self.s_address = s_address

    def set_s_status(self, s_status):
        self.s_status = s_status

    def set_s_sales_tax_percentage(self, s_sales_tax_percentage):
        self.s_sales_tax_percentage = s_sales_tax_percentage

    # accessors of store class
    def get_s_name(self):
        return self.s_name

    def get_s_address(self):
        return self.s_address

    def get_s_status(self):
        return self.s_status

    def get_s_sales_tax_percentage(self):
        return self.s_sales_tax_percent

    # returns true if store is open else false
    def is_store_open(self):
        if (status.lower() == "open"):
            return True

        return False

    # abstract function to calculate total sales tax
    def calculate_total_sales_tax(self):
        pass

    # abstract function to calculate total sales
    def calculate_total_sales(self):
        pass


