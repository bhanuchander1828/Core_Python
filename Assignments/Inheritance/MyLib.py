'''
ITMD 513 : Assignment-Inheritance - Bhanu kureti
Summary : This program will create Candles class with attributes color, height, price which inherited in sub class
ScentedCandles
'''


# Candles class is created with data fields color, height and price
class Candles:
    def __init__(self, color, height):  # Constructor
        self.color = color
        self.height = height

    # Get methods for the data fields
    def getColor(self):
        return self.color

    def getHeight(self):
        return self.height

    def getPrice(self):
        return self.price

    # Set methods created for the data fields
    def setColor(self, color):
        self.color = color

    def setHeight(self, height):
        self.height = height
        # Calculating price value based on the height value.
        self.price = (self.height / 5) * 2  # Given price is $2 / 5 Centimeters


# ScentedCandles subclass is created which has scent data field and inherits data fields from the Candles superclass.
class ScentedCandles(Candles):
    def __init__(self, color, height, scent):
        Candles.__init__(self, color, height)           # Invoke _init_from the parent Candles class
        self.scent = scent

    # Get method for scent filed
    def getScent(self):
        return self.scent

    # Set method for scent field
    def setScent(self, scent):
        return self.scent

    def setHeight(self, height):
        self.height = height
        # Calculating price value based the height value
        self.price = (self.height / 7) * 3            # Here price values is $3 / 7 centimeters
