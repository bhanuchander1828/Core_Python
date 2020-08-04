"""
ITMD 513 : Classes - HomeWork - Bhanu Kureti
Summary : In this program Checkout_Register will implement a class that provides same type functionality
of real life checkout registers
"""


class Checkout_Register:
    currencysymbol = ""
    salesTax = 0
    total_transactions = 0
    total_amt_for_transactions = 0
    num_of_cash_transactions = 0
    total_amt_for_cash_transactions = 0
    num_of_card_transactions = 0
    total_amt_for_card_transactions = 0
    productList = {}

    def __init__(self, symbol, taxes):
        """
        Constructor for checkout register class
        parameters:
        symbol: The symbol of currency.
        taxes: The sales tax for the transaction.
        """
        self.currencysymbol = symbol
        self.salesTax = taxes

    # Accessor methods of checkout register class
    def getCurrencySymbol(self):
        return self.currencysymbol  # Returns Currency symbol

    def getSalesTax(self):
        return self.salesTax  # Returns sales tax of transaction

    def getTotalTransactionsNumber(self):
        return self.total_transactions  # Returns total number of transactions

    def getTotalTransactionsAmount(self):
        return self.total_amt_for_transactions  # Returns the total amount for whole transactions

    def getTotalCashTransactionsNum(self):
        return self.num_of_cash_transactions  # Returns the total number of cash transactions

    def getTotalCashTransactionsAmount(self):
        return self.total_amt_for_cash_transactions  # Returns the total amount for cash transactions

    def getTotalCardTransactionsNum(self):
        return self.num_of_card_transactions  # Returns the total number of card transactions

    def getTotalCardTransactionsAmount(self):
        return self.total_amt_for_card_transactions  # Returns the total amount for card transactions

    def getProductList(self):
        return self.productList  # returns the products list

    # Setter methods of checkout register class

    def setProductList(self, items1):
        self.productList = items1  # set the products list

    def setCurrencySymbol(self, symbol):
        self.currencysymbol = symbol  # set Currency symbol

    def setSalesTax(self, tax):
        self.salesTax = tax  # set tax of transaction

    def setTotalTransactionsNumber(self, totalTrans):
        self.total_transactions = totalTrans  # set total number of transactions

    def setTotalTransactionsAmount(self, totaltransAmt):
        self.total_amt_for_transactions = totaltransAmt  # set the total amount for whole transactions

    def setTotalCashTransactionsNum(self, totalCashTrans):
        self.num_of_cash_transactions = totalCashTrans  # set the total number of cash transactions

    def setTotalCashTransactionsAmount(self, totalCashAmt):
        self.total_amt_for_cash_transactions = totalCashAmt  # set the total amount for cash transactions

    def setTotalCardTransactionsNum(self, totalCardTrans):
        self.num_of_card_transactions = totalCardTrans  # set the total number of card transactions

    def setTotalCardTransactionsAmount(self, totalCardAmt):
        self.total_amt_for_card_transactions = totalCardAmt  # set the total amount for card transactions

    # This method will calculate the total amount of transaction
    def calculateTotalAmount(self):
        total = 0
        #print(self.productList)
        for i in self.productList:
            total += self.productList[i]
        return total

    # This method will calculate tax on total transaction
    def calculateSalesTax_on_transactions(self):
        return self.salesTax * self.calculateTotalAmount() / 100.0

    # This method will return total amount with adding tax to it
    def calculateTotalAmountWithTax(self):
        return self.calculateTotalAmount() + self.calculateSalesTax_on_transactions()

    # This method will return string which is receipt of the transaction
    def createReceipt(self):
        itemsList = "Items in your Transaction: \n"
        total = 0
        # Returns the list of items purchased
        for i in self.productList:
            itemsList += str(i) + "  -  " + self.currencysymbol + " " + str(self.productList[i]) + "\n"
            total += self.productList[i]

        tax = self.calculateSalesTax_on_transactions()
        itemsList += "--------------------\nTotal  -  " + self.currencysymbol + str(total) + "\n"
        itemsList += "\nSales Tax  -  " + self.currencysymbol + str(tax) + "\n"
        total += tax
        itemsList += "\n" + "Total Price -" + self.currencysymbol + " " + str(total)
        return itemsList

    # This method will process cash transaction

    def processCash_transaction(self, cash):
        cash = float(cash)
        self.total_amt_for_transactions += cash
        self.total_transactions += 1
        self.total_amt_for_cash_transactions += cash
        self.num_of_cash_transactions += 1
        AmountDue = self.calculateTotalAmountWithTax()
        # If cash given by customer is more than Due amount, remaining change is given to the customer
        if cash > AmountDue:
            print(self.createReceipt())
            change = cash - AmountDue
            print("\n\nPlease give the customer remain change : "+str(change))
            return change
        # If cash given by customer is less than Due amount, will returns the money owed by customer
        elif cash < AmountDue:
            AmountOwe = AmountDue - cash
            print("Customer need to pay the due amount which is : "+str(AmountOwe))
            exit()
            return AmountOwe
        else:
            print(" Successfully transaction completed!!\n Thanks for visiting:)")
            return 0

    # This method will process card transactions

    def processCard_transaction(self, card_type):
        # if card type is other than debit or credit  print invalid message
        if (card_type == "credit" or card_type == "debit"):
            AmountDue = self.calculateTotalAmountWithTax()  # proceed with credit/debit card do the transactions
            self.total_amt_for_transactions += AmountDue
            self.total_transactions += 1
            self.total_amt_for_card_transactions += AmountDue
            self.num_of_card_transactions += 1
            # return the amount charged and print receipt
            print(self.createReceipt())
            return AmountDue
        else:
            print("\n Invalid card type provided, please provide either a credit or debit card")
            return None

# main Function where programme is called
def main():
    checkout = Checkout_Register("$", 5)
    # dictionary shows the items and their prices
    items = {"pens": 10, "books": 200, "Bag": 500}
    checkout.setProductList(items)

    charged = checkout.processCard_transaction("credit")
    print("\nYour card has been charged -"+str(checkout.currencysymbol)+" "+str(charged))

    # For cash function please uncomment the below code and use it for cash type and enter value of amount.

    #cashGiven = checkout.processCash_transaction(500)


main()

