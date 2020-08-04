
# Importing numpy and pandas modules

import numpy as np
import pandas as pd

# Creating DataFrame from the Dictionary we created

temperatures = pd.DataFrame({"Maxine": [98, 96,94.6], "James": [100.2, 92.8,98.7], "Amanda": [94.8, 97.4, 97.4]},
                  index=[1,2, 3])
print(temperatures)


# Changing the index values to Morning, Afternoon, Evening

temperatures.index = ["Morning", "Afternoon", "Evening"]
print(temperatures)

# Selecting the temperatures of column Maxine
print(temperatures.loc[:,'Maxine'])


# Selecting the temperatures of Row Morning
print(temperatures.loc['Morning',:])

# Selecting the temperatures of rows Morning and Evening
print(temperatures.loc[['Morning', 'Evening'],:])

# Selecting the temperatures of columns Maxine and Amanda
print(temperatures.loc[:,['Maxine','Amanda']])

# selecting temperature value of morning, afternoon rows and amanda and maxine columns
print(temperatures)
print(temperatures.loc[['Morning','Afternoon'],['Maxine','Amanda']])


# Statistics of the temperatures
temperatures.describe()

# Transpose the index to columns and columns to index for temperatures dataframe
Temp_transpose = temperatures.transpose()
print(Temp_transpose)

# Sorting the temperatures dataframe columns in alphabetical order
temp_sort=temperatures.sort_index(axis=1)
print(temp_sort)

