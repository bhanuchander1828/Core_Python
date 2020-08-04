'''
ITMD 513 : Seaborn - HW7 - Bhanu kureti
Summary : This program will perform data Visualizations using Seaborn
'''

# Importing the libraries
import pathlib
import pandas as pd
import seaborn as sns; sns.set(style="darkgrid")
import matplotlib.pyplot as plt

# Functions to create data visualizations

# Function for scatter plot
def createSPlotA(df_W):
    # Plotting Scatter plot using seaborn
    sp = sns.scatterplot(x="total_bill", y="tip", data=df_W)

    # Title for scatter plot
    plt.title(" Scatter Plot : Total_Bill Vs Tip ")

    # Display the Scatter plot
    plt.show()

# Function for scatter plot
def createSPlotB(df_W):
    # Plotting Scatter plot using seaborn
    sp = sns.scatterplot(x="total_bill", y="tip", hue="smoker", style="smoker", size="size",
                         sizes=(10, 300), legend="full", data=df_W)

    # Title for scatter plot
    plt.title(" Scatter Plot : Total_Bill Vs Tip among Smokers ")

    # Display the Scatter plot
    plt.show()

# Function for Bar plot
def createBPlotC(df_W):
    # Plotting Bar plot using seaborn
    sp = sns.catplot(x="day", y="tip", kind="bar", data=df_W)

    # Title for scatter plot
    plt.title(" Bar Plot : Average Tips of day in week ")

    # Display the Scatter plot
    plt.show()

# Function for scatter plot
def createSPlotD(df_W):
    # Plotting Scatter plot using seaborn
    sp = sns.scatterplot(x="total_bill", y="tip", hue="time", style="time",
                         size="size", sizes=(10, 300), legend="full", data=df_W)

    # Title for scatter plot
    plt.title(" Scatter Plot : Average Tips of the day per week over time ")

    # Display the Scatter plot
    plt.show()

# Function for Line plot
def createLinePlotE(df_F):
    # Plotting Line plot using seaborn
    sp = sns.lineplot(x="year", y="passengers", palette="hot", hue="month", estimator="mean", data=df_F)

    # Title for scatter plot
    plt.title(" Line Plot : Average passengers per month in a year ")

    # Display the Scatter plot
    plt.show()

# Function for bar plot
def createBarPlotF(df_T):
    # Plotting Bar plot using seaborn
    sns.catplot(x="Sex", data=df_T, hue="Pclass", col="Survived", kind="count", height=4, aspect=.7)

    # Title for scatter plot
    #plt.title(" Bar Plot : Count of observations in each categorical bin ")

    # Display the Scatter plot
    plt.show()

# Main function where program start execution
def main():

    # File paths and folder information
    fileDirectory=pathlib.Path(__file__).parent.absolute()
    workerstips_F = str(fileDirectory) + '//workerstips.csv'
    flightsData_F = str(fileDirectory) + '//flightsData.csv'
    titanic_F = str(fileDirectory) + '//titanic.csv'

    # Create Data frames
    df_WorkersTips = pd.read_csv(workerstips_F)
    df_FlightsData = pd.read_csv(flightsData_F)
    df_Titanic = pd.read_csv(titanic_F)

    # a) Create a scatter plot 
    createSPlotA(df_WorkersTips)

    # b) Create a scatter plot to differentiate between Smokers and Non Smokers
    createSPlotB(df_WorkersTips)

    # c) Create a bar plot
    createBPlotC(df_WorkersTips)

    # d) Create a scatter plot to differentiate between lunch and dinner time
    createSPlotD(df_WorkersTips)

    # e) Create a line plot between avg number of passengers per year per month
    createLinePlotE(df_FlightsData)

    # f) Create bar plot for titanic categorical counts
    createBarPlotF(df_Titanic)

# Call the main() function
main()
