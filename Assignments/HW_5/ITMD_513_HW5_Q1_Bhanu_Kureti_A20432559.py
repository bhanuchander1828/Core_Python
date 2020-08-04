'''
ITMD 513 : Assignment 5 - Bhanu kureti
Summary : This program will plot line and Bar Graph for the weekly gas averages
'''

# Importing the modules required for this program
import matplotlib.pyplot as plt
import pathlib
import os

# This function will give details of x and y label and title of graph
def graphLabels(x_axis, y_axis, plot_Title):
 plt.xlabel(x_axis)
 plt.ylabel(y_axis)
 plt.title(plot_Title)

# This function will create Bar graph
def creatBarGraph(xAxis , yAxis):
 # Add Labels to the plots
 plt.bar(xAxis , yAxis)
 graphLabels('Week Index',' Gas Average', 'weekly Gas Averages')
 plt.show()

# This function will create line graph
def creatlineGraph(xAxis , yAxis):
 plt.plot(xAxis , yAxis)
 plt.grid(True)
 graphLabels('Week Index',' Gas Average', 'weekly Gas Averages')
 plt.show()

# Main Function where program starts execution
def main():

 # File Path where we find file and folder
 filesDirectory = pathlib.Path('_file_').parent.absolute()
 file = str(filesDirectory)+'/1994_Weekly_Gas_Averages.txt'

 # Empty Lists to get content
 weekIndexX = []
 gasAverageY = []


 if os.path.isfile(file):
    inputFile = open(file, "r")
    data_content = inputFile.read()

    gasAverageY = [float(x) for x in data_content.split()]
    for i in range(0,len(gasAverageY)):
      weekIndexX.append(i+1)

    creatBarGraph(weekIndexX, gasAverageY)
    creatlineGraph(weekIndexX, gasAverageY)
    
    #closing the file
    inputFile.close()
 else:
   print('Input File is not found')
 exit

# call main function
main()