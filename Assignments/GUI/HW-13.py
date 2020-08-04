"""
This is creating a GUI having different coins and a button for calculating the
total value.It also validates the user input for the correct values.
"""


from tkinter import *
import tkinter.messagebox

r = Tk()
r.title("Change Counter")

heading = Label(r, text="Enter *** the number of each coin type and hit,Compute:").grid(row=0,column=1)

dollars = Label(r ,text = "Dollars:").grid(row = 1,column = 1)
dollars1 = Entry(r)
dollars1.grid(row = 1,column = 2)

dollarscon = Label(r ,text = "Dollar Value:$").grid(row = 1,column = 4)
dollarscon1 = Label(r,text="0.00",width=5)
dollarscon1.grid(row = 1 , column = 5)

halfdollars = Label(r ,text = "Half Dollar:").grid(row = 2,column = 1)
halfdollars1 = Entry(r)
halfdollars1.grid(row = 2,column = 2)

halfdollarscon = Label(r ,text = "Half Dollar Value:$").grid(row = 2,column = 4)
halfdollarscon1 = Label(r,text="0.00",width=5)
halfdollarscon1.grid(row = 2 , column = 5)

quarters = Label(r ,text = "Quarters:").grid(row = 3,column = 1)
quarters1 = Entry(r)
quarters1.grid(row = 3,column = 2)

quarterscon = Label(r ,text = "Quarter Value:$").grid(row = 3,column = 4)
quarterscon1 = Label(r,text="0.00",width=5)
quarterscon1.grid(row = 3 , column = 5)

dimes = Label(r ,text = "Dimes:").grid(row = 4,column = 1)
dimes1 = Entry(r)
dimes1.grid(row = 4,column = 2)

dimescon = Label(r ,text = "Dime Value:$").grid(row = 4,column = 4)
dimescon1 = Label(r,text="0.00",width=5)
dimescon1.grid(row = 4,column = 5)

nickels = Label(r ,text = "Nickels:").grid(row = 5,column = 1)
nickels1 = Entry(r)
nickels1.grid(row = 5,column = 2)

nickelscon = Label(r ,text = "Nickel Value:$").grid(row = 5,column = 4)
nickelscon1 = Label(r,text="0.00",width=5)
nickelscon1.grid(row = 5,column = 5)

pennies = Label(r ,text = "Pennies:").grid(row = 6,column = 1)
pennies1 = Entry(r)
pennies1.grid(row = 6,column = 2)

penniescon = Label(r ,text = "Penny Value:$").grid(row = 6,column = 4)
penniescon1 = Label(r,text="0.00",width=5)
penniescon1.grid(row = 6,column = 5)

totalchangevalue = Label(r ,text = "Total Change Value:$").grid(row = 7,column = 4)
totalchangevalue1 = Label(r,text="0.00",width=5)
totalchangevalue1.grid(row = 7,column = 5)

def computeTotal():
    dollar = (dollars1.get())
    halfdollar = (halfdollars1.get())
    quarter = (quarters1.get())
    dime = (dimes1.get())
    nickel = (nickels1.get())
    pennies = (pennies1.get())
    total=0.00

    if((dollar.isdigit() or halfdollar.isdigit() or quarter.isdigit() or dime.isdigit() or nickel.isdigit() or pennies.isdigit()) and
       (dollar != "" and halfdollar!="" and quarter!="" and dime!="" and nickel!="" and pennies!="")):

          if(float(dollar)>0.0):
            total = total+(float(dollar))
            a = float(dollar)
            dollarscon1.configure(text= round(a,2))

          if(float(halfdollar)>0.0):
            total = total+(float(halfdollar)*0.50)
            b = float(halfdollar)*0.50
            halfdollarscon1.configure(text= round(b,2))
            
          if(float(quarter)>0.0):
            total = total+(float(quarter)*0.25)
            c = float(quarter)*0.25
            quarterscon1.configure(text= round(c,2))

  
          if(float(dime)>0.0):
            total = total+(float(dime)*0.10)
            d = float(dime)*0.10
            dimescon1.configure(text= round(d,2))
      
   
          if(float(nickel)>0.0):
            total = total+(float(nickel)*0.05)
            e = float(nickel)*0.05
            nickelscon1.configure(text= round(e,2))

     
          if(float(pennies)>0.0):
            total = total+(float(pennies)*0.01)
            f = float(pennies)*0.01
            penniescon1.configure(text= round(f,2))
        
          totalchangevalue1.configure(text=round(total,2))
          return True
    else:
        tkinter.messagebox.showwarning("Wrong Data","Invalid Data,Numbers are only allowed and Enter all the values")
        dollars1.delete(0,END)
        halfdollars1.delete(0,END)
        quarters1.delete(0,END)
        dimes1.delete(0,END)
        nickels1.delete(0,END)
        pennies1.delete(0,END)
        return False

btn = Button(r, text="Compute", command=computeTotal).grid(row=8,column=2)

r.mainloop() 

