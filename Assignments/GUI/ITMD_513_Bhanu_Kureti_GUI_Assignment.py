"""
ITMD 513 : Assignment-Polymorphism - Bhanu kureti
Summary : This program will create GUI which has different coins and buttons to calculate the total value. It also
contains input validations from the user
"""

from tkinter import *
import tkinter.messagebox

r = Tk()
r.title("Currency Counter")

heading = Label(r, text="Please enter the number of each coin type and enter Compute:").grid(row=0, column=1)

dollars = Label(r, text="Dollars:").grid(row=1, column=1)
dollars_1 = Entry(r)
dollars_1.grid(row=1, column=2)

dollars_coin = Label(r, text="Dollar Value:$").grid(row=1, column=4)
dollars_coin1 = Label(r, text="0.00", width=5)
dollars_coin1.grid(row=1, column=5)

half_dollars = Label(r, text="Half Dollar:").grid(row=2, column=1)
half_dollars1 = Entry(r)
half_dollars1.grid(row=2, column=2)

halfdollars_coin = Label(r, text="Half Dollar Value:$").grid(row=2, column=4)
halfdollars_coin1 = Label(r, text="0.00", width=5)
halfdollars_coin1.grid(row=2, column=5)

quarters = Label(r, text="Quarters:").grid(row=3, column=1)
quarters_1 = Entry(r)
quarters_1.grid(row=3, column=2)

quarters_coin = Label(r, text="Quarter Value:$").grid(row=3, column=4)
quarters_coin1 = Label(r, text="0.00", width=5)
quarters_coin1.grid(row=3, column=5)

dimes = Label(r, text="Dimes:").grid(row=4, column=1)
dimes_1 = Entry(r)
dimes_1.grid(row=4, column=2)

dimes_coin = Label(r, text="Dime Value:$").grid(row=4, column=4)
dimes_coin1 = Label(r, text="0.00", width=5)
dimes_coin1.grid(row=4, column=5)

nickels = Label(r, text="Nickels:").grid(row=5, column=1)
nickels_1 = Entry(r)
nickels_1.grid(row=5, column=2)

nickels_coin = Label(r, text="Nickel Value:$").grid(row=5, column=4)
nickels_coin1 = Label(r, text="0.00", width=5)
nickels_coin1.grid(row=5, column=5)

pennies = Label(r, text="Pennies:").grid(row=6, column=1)
pennies_1 = Entry(r)
pennies_1.grid(row=6, column=2)

pennies_coin = Label(r, text="Penny Value:$").grid(row=6, column=4)
pennies_coin1 = Label(r, text="0.00", width=5)
pennies_coin1.grid(row=6, column=5)

totalchangeamount = Label(r, text="Total Change Amount:$").grid(row=7, column=4)
totalchangeamount1 = Label(r, text="0.00", width=5)
totalchangeamount1.grid(row=7, column=5)


def calculateTotal():
    dollar = (dollars_1.get())
    halfdollar = (half_dollars1.get())
    quarter = (quarters_1.get())
    dime = (dimes_1.get())
    nickel = (nickels_1.get())
    pennies = (pennies_1.get())
    total = 0.00

    if ((
            dollar.isdigit() and halfdollar.isdigit() and quarter.isdigit() and dime.isdigit() and nickel.isdigit() and
            pennies.isdigit()) and (dollar != "" and halfdollar != "" and quarter != "" and dime != "" and
            nickel != "" and pennies != "")):

        if float(dollar) > 0.0:
            total = total + (float(dollar))
            a = float(dollar)
            dollars_coin1.configure(text=round(a, 2))

        if float(halfdollar) > 0.0:
            total = total + (float(halfdollar) * 0.50)
            b = float(halfdollar) * 0.50
            halfdollars_coin1.configure(text=round(b, 2))

        if float(quarter) > 0.0:
            total = total + (float(quarter) * 0.25)
            c = float(quarter) * 0.25
            quarters_coin1.configure(text=round(c, 2))

        if float(dime) > 0.0:
            total = total + (float(dime) * 0.10)
            d = float(dime) * 0.10
            dimes_coin1.configure(text=round(d, 2))

        if float(nickel) > 0.0:
            total = total + (float(nickel) * 0.05)
            e = float(nickel) * 0.05
            nickels_coin1.configure(text=round(e, 2))

        if float(pennies) > 0.0:
            total = total + (float(pennies) * 0.01)
            f = float(pennies) * 0.01
            pennies_coin1.configure(text=round(f, 2))

        totalchangeamount1.configure(text=round(total, 2))
        return True
    else:
        tkinter.messagebox.showwarning("Invalid Data", "Numbers only allowed and Enter the correct values")
        dollars_1.delete(0, END)
        half_dollars1.delete(0, END)
        quarters_1.delete(0, END)
        dimes_1.delete(0, END)
        nickels_1.delete(0, END)
        pennies_1.delete(0, END)
        return False


btn = Button(r, text="Compute", command=calculateTotal).grid(row=8, column=2)

r.mainloop()

