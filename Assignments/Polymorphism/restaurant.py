"""
ITMD 513 : Assignment- Polymorphism - Bhanu kureti
Summary : This program will create Restaurant class with attributes current_occupancy,
maximum occupancy, price_per_person and inherits attributes and methods of store class
"""
# Importing Store class from Store.py program
from Store import Store


class Restaurant(Store):

    # constructor
    def __init__(self, s_name, s_address, s_status, s_sales_tax_percentage, r_max_occupancy, r_price_per_person):

        super().__init__(s_name, s_address, s_status, s_sales_tax_percentage)
        self.r_max_occupancy = r_max_occupancy
        self.r_total_num_served = 0
        self.r_current_occupancy = 0
        self.r_price_per_person = r_price_per_person

    # function will take number of people to be seated as input and returns true if the people can be seated else false
    def seat_patrons(self, num_of_people):
        # if current occupancy + num of people less that maximum occupancy, then it returns True
        if ((self.r_current_occupancy + num_of_people) <= self.r_max_occupancy):
            print("Welcome to %s" % (self.get_s_name()))
            self.r_current_occupancy += num_of_people
            return True
        else:  # if num of people cannot be seated, return false
            print("We are at capacity, we appreciate your patience")
            return False

    # function will take number of people to be serve as input and returns the number of people served
    def serve_patrons(self, num_of_people):
        self.r_total_num_served += num_of_people  # add num_people to num_served and return the updated value
        return self.r_total_num_served

    # function will take number of people leaving the restaurant and returns the current_occupancy
    def checkout_patrons(self, num_of_people):
        self.r_current_occupancy -= num_of_people  # remove the num_people from current_occupancy
        return self.r_current_occupancy  # return the updated current_occupancy

    # mutator of restaurant class
    def set_r_price_per_person(self, r_price_per_person):
        self.r_price_per_person = r_price_per_person

    # accessor of restaurant class
    def get_r_price_per_person(self):
        return self.r_price_per_person

    # calculate and return the total sales tax
    def calculate_total_sales_tax(self):
        return float(self.calculate_total_sales() * self.get_s_sales_tax_percentage()) / 100

    # calculate and return the total sales
    def calculate_total_sales(self):
        return float(self.r_total_num_served * self.r_price_per_person)
