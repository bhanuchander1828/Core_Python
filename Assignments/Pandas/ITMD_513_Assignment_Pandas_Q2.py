
#Importing the modules required for this program
import csv
import pandas as pd
import numpy as np


#Importing the CSV file
data = pd.read_csv('/Users/bhanuchanderkureti/Bhanu/ITMD_513/Assignments/Pandas/titanic.csv')
df = pd.DataFrame(data)


#List columns and rows of data frame
df.head()

#Total number of passengers
print("Total number of passengers:\n" + str(df.PassengerId.count()))

# male and female passengers count 
print("Total number of male and female passengers:\n" + str(df['Sex'].value_counts))

# Average age of all populations
                                                            
print("Average age of passengers:\n" + str(df.Age.mean()))


# Number of Passengers under Age 21
child = df[df.Age < 21.00]
print("The Number of Passengers less than age 21 :\n" + str(len(child)))


# Assuming If Survive = 1 as survived and Survived = 0 as Un Survived

print("Sum of Survived: "+ str(sum(df["Survived"]==0))) # Number of Survived
print("Sum of UnSurvived: "+ str(sum(df["Survived"]==1))) # Number of UnSurvived
print("Sum of males Survived: "+ str(sum((df["Survived"]==1) & (df["Sex"]=='male')))) # Number of male's Survived
print("Sum of females Survived: "+ str(sum((df["Survived"]==1) & (df["Sex"]=='female')))) # Number of female's Survived
print("Sum of males unSurvived: "+ str(sum((df["Survived"]==0) & (df["Sex"]=='male')))) # Number of male's UnSurvived
print("Sum of females UnSurvived: "+ str(sum((df["Survived"]==0) & (df["Sex"]=='female')))) # Number of female's UnSurvived


# Name and Age of Youngest Age person who is survived
df_sur = df[df["Survived"]==1]
df_sur = df_sur.loc[df_sur["Age"]==min(df_sur.Age)]
print('Youngest age to survive the Titanic mishap is :\n'+ str(df_sur.Age.to_string(index=False)) + str(df_sur["Name"].to_string(index=False)))


# Name and Age of Oldest Age person who is survived
df_sur = df[df["Survived"]==1]
df_sur = df_sur.loc[df_sur["Age"]==max(df_sur.Age)]
print('oldest age to survive the Titanic mishap is :\n '+ str(df_sur.Age.to_string(index=False)) + str(df_sur["Name"].to_string(index=False)))

# Names of people who are survived
print('\ng) Names of all the people who survived:\n'+ str(df.loc[(df['Survived']==1), 'Name']))



