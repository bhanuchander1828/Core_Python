#!/usr/bin/env python
# coding: utf-8

# In[1]:


'''
ITMD 513: Assignment 2 - Bhanu Kureti
Description: This program will allow user to choose between two operations, Average or Area of the triangle
    I) Average: User has to enter 5 test scores to find the average and the program will calculates the average
                and find out the grade to be awarded for that score
    II) Area of Triangle: This program will find the Area of Triangle if user enters three different sides of a traingle
'''

import math

#User Input Function

def userValidation():
    loop = True
    while loop == True:
        userInput = input('\nChoose from the menu: \n1) Test Average and Grade\n2) Area of a triangle\n0) Exit\nEnter the option: ')
        if userInput.isnumeric():
            userInput = int(userInput)
            if userInput < 3 and userInput >= 0:
                loop = False
            else:
                print ("\nUser Inputs must be 0 | 1 | 2\n")
                continue
        else:
            print ("\nUser selection must be numbers 0 | 1 | 2\n")
            continue
    return userInput

#Function for user's input for 5 test scores

def userInputScores_5():
    testScores = []
    for index in range(5):
        testNumber = index + 1
        loop = True
        while loop == True:
            userInput_5 = input('Please enter the scores for test '+str(testNumber)+': ')
            if userInput_5.isnumeric():
                userInput_5 = int(userInput_5)
                if userInput_5 < 0 or userInput_5 > 101:
                    print ("\nTest Score(s) should only be between 0 and 100(inclusive)!\n")
                    continue
                else:
                    loop = False
            else:
                print ("\nTest scores must be positive numbers only!\n")
                continue
        testScores.insert(index, userInput_5)
    return testScores

#Function to calculate the average of test scores
def average(testScoresListArg):
    lengthOfList = len(testScoresListArg)
    sumOfTestScores = 0
    for score in testScoresListArg:
        sumOfTestScores += score
    averageScore = sumOfTestScores / lengthOfList

    return averageScore

#Function to find the grade of each test score
def Assign_grade(testScoreArg):
    Grade_letter = ''
    if testScoreArg > 89:
        Grade_letter = 'A'
    elif testScoreArg > 79 and testScoreArg < 90:
        Grade_letter = 'B'
    elif testScoreArg > 69 and testScoreArg < 80:
        Grade_letter = 'C'
    elif testScoreArg > 59 and testScoreArg < 70:
        Grade_letter = 'D'
    elif testScoreArg < 60:
        Grade_letter = 'F'
    else:
        Grade_letter = 'N/A'
    
    return Grade_letter

#Function for user's input for triangle co-ordinates
def userInputPoints_3():
    trianglePoints = []
    for index in range(3):
        CoordNumber = index + 1
        loop = True
        while loop == True:
            userInputForX = input('Please enter the value for Point '+str(CoordNumber)+': ')
            if userInputForX.isnumeric():
                '''
                while loop == True:
                    userInputForY = input('Please enter the value for Y'+str(CoordNumber)+': ')
                    if userInputForY.isnumeric():
                        loop = False
                    else:
                        print ("\npoint must be numeric only!\n")
                        continue
                '''
                userInputForX = int(userInputForX)
                if userInputForX < 0:
                    print ("\nPoint should only be positive values!!")
                    continue
                else:
                    loop = False
            else:
                print ("\npoint must be positive !\n")
                continue
        trianglePoints.append(userInputForX)
        #triangleCoords.append(userInputForY)
    return trianglePoints


#Function to calculate the s value
def cal_SValue(threePointsListArg):
    '''
    X1 = int(threePointsListArg[0])
    Y1 = int(threePointsListArg[1])
    X2 = int(threePointsListArg[2])
    Y2 = int(threePointsListArg[3])
    X3 = int(threePointsListArg[4])
    Y3 = int(threePointsListArg[5])
    sValue = (((X1*Y2)+(X2*Y3)+(X3*Y1))-((X1*Y3)-(X2*Y1)-(X3*Y2)))/2
    '''
    sumOfSides = 0
    for point in threePointsListArg:
        sumOfSides += point
    sValue = sumOfSides/2

    return sValue

#Function to calculate the area of the triangle
def cal_TrnglArea(valueOfSArg, threePointsListArg):
    side1 = threePointsListArg[0]
    side2 = threePointsListArg[1]
    side3 = threePointsListArg[2]

    area = math.sqrt(valueOfSArg*(valueOfSArg - side1)*(valueOfSArg - side2)*(valueOfSArg - side3))

    return area

#main() function
def main():
    choice = userValidation()
    if choice == 1:
        #Test Average and grade
        testScoresList = userInputScores_5()
        testAverage = average(testScoresList)
        testNumber = 1
        print("\n")
        for score in (testScoresList):
            score = int(score)
            grade = Assign_grade(score)
            print ("Grade of the student for Test "+str(testNumber)+" is: ", grade)
            testNumber += 1
        
        print("\nAverage test score for this student is: %.2f" %(testAverage))

    elif choice == 2:
        #Area of triangle
        threePointsList = userInputPoints_3()
        valueOfS = cal_SValue(threePointsList)
        areaOfTriangle = cal_TrnglArea(valueOfS, threePointsList)
        print ("Area of the triangle with the given co-ordinates is: %.2f" %(areaOfTriangle))

    else:
        #exit the program
        print("The Program exists.")
        exit()

#Call the main function
main()


# 

# # 
