'''
ITMD 513 : Assignment-Inheritance - Bhanu kureti
Summary : This program will create application program that instantiates an
object of each type from myLib and display the details.
'''

# Importing Candles and ScentedCandles classes
from MyLib import Candles, ScentedCandles

print("**********Candles object*********")
candle1 = Candles("violet", 14.6)
candle1.setHeight(14.6)
print("The details of the candle are:", "\nHeight:", candle1.getHeight(), "\ncolor:", candle1.getColor(),
      "\nPrice:", candle1.getPrice())


print("\n**********ScentedCandles object*********")
candle2 = ScentedCandles("white", 14.6, "Safran")
candle2.setHeight(8)
print("The details of the ScentedCandle are:", "\nHeight:", candle2.getHeight(), "\ncolor:", candle2.getColor(),
      "\nPrice:", candle2.getPrice(), "\nScent:", candle2.getScent())

