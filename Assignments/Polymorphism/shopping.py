"""
ITMD 513 : Assignment- Polymorphism - Bhanu kureti
Summary : This shopping.py program will be used to test the restaurant and grocery stores program
"""
# Importing the Restaurant and GroceryStore classes from restaurant and grocery_store programs
from restaurant import Restaurant
from grocery_store import GroceryStore


# main function where execution starts
def main():
    print("\n------Restaurant class Testing------")
    storeR = Restaurant("CumIn Restaurant", "28, State Street", "open", 6.25, 150, 14.99)
    print("%s is %s" % (storeR.get_s_name(), storeR.get_s_status()))
    print(storeR.seat_patrons(75))
    print("Number of people served: %d " % storeR.serve_patrons(25))
    print("Current occupancy: %d" % storeR.checkout_patrons(30))
    print("Total sales : $%.2f" % (float(storeR.calculate_total_sales())))
    print("Total sales tax: $%.2f" % (float(storeR.calculate_total_sales_tax())))
    print("Total Amount due: $%.2f" % (storeR.calculate_total_sales() + storeR.calculate_total_sales_tax()))
    print("\n----Checking when input value more than capacity----")
    print(storeR.seat_patrons(185))
    print("Testing Restaurant class is done\n")
    print("--------------------------------------------")
    print("GroceryStore class Testing")
    storeG = GroceryStore("AllInOne Grocery Store", "2801 S king drive", "open", 6.45, "independent")
    print("Grocery Store %s is %s" % (storeG.get_s_name(), storeG.get_s_status()))
    print("Total revenue of store after selling 4 rice bags @14.75 = $%.2f " % (storeG.sell_item(4, 14.75)))
    print("Total revenue of store after selling 6 milk @2.75 = $%.2f" % (storeG.sell_item(6, 2.75)))
    print("Total revenue of store after selling 2 Bread @1.75 = $%.2f" % (storeG.sell_item(2, 1.75)))
    print("\nTotal sales tax: $%.2f" % (storeG.calculate_total_sales_tax()))
    print("Total cost of sales with tax: $%.2f" % (storeG.calculate_total_sales_tax() + storeG.calculate_total_sales()))
    print("\n----checking the Status attribute of store ----")
    storeG.set_s_status("closed")
    print("Grocery Store %s is %s" % (storeG.get_s_name(), storeG.get_s_status()))
    print("End of testing GroceryStore class")


# call the main function
main()
