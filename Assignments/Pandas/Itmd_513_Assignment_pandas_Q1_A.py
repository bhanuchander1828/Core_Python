
import numpy as np
import pandas as pd
import random


# creating a series with given elements
ds = pd.Series([7,11,13,17])
print(ds)


# creating series with five elements that all are 100 
ds1 = pd.Series([100,100,100,100,100])
print(ds1)


# creating series from random numbers between(1,100)
ds2 = pd.Series(random.sample(range(0,100), 20))
# Statistics of the numbers selected randomly
print(ds2.describe())


# creating the Series temperatures from the given values and index
Temperatures = pd.Series(np.array([98.6, 98.9, 100.2,97.9]),index=["Julie",'Charlie', 'Sam' ,'Andrea'])
print(Temperatures)


# creating  Series from dictionary which takes the values and index from above question.
temp_dict = pd.Series({"Julie" : 98.6,"Charlie": 98.9 ,"Sam": 100.2, "Andrea": 97.9})
print(temp_dict)



