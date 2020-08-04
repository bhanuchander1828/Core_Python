"""
ITMD 513 : Dictionaries - HomeWork - Bhanu kureti
Summary : In this program we will create dictionary files and perform some operations like adding and changing the values
from the dictionary
"""

import re

# This function creates a dictionary and then writes the data to the text file
import sys

from pip._vendor.distlib.compat import raw_input


def write_file():
    try:
        print("Write a dictionary to a file")
        dict = {"Bhanu": 1111, 'Nandu': 2222, 'Raju': 3333, 'Daksha': 4444}
        f = open("name_id.txt", "w")
        f.write(str(dict))
        f.close()
    except Exception:
        print("Exception Occurred!!!")


# This function will be used by all the functions for reading the data from the text file
def readDataForAllFuncs():
    try:
        f = open("name_id.txt", "r")
        for lines in f.readlines():
            # print lines
            dict = eval(lines)
        return dict
        f.close()
    except Exception:
        print("Exception Occurred!!")


# This function will be used by all the functions for writing the data to the text file
def writeDataForAllFuncs(nameid_d):
    try:
        f = open("name_id.txt", "w")
        f.write(str(nameid_d))
        f.close()
    except Exception:
        print("Exception Occurred!!")


# This function will be used by all the functions for reading the data from the text file
def read_file():
    try:
        print("LookUp for a person's Id Number")
        nameid_d = readDataForAllFuncs()
        print(nameid_d)
    except Exception:
        print("Exception Occurred!!!")


# This function will be used to add the new record of the name and person's id to the dictionary and then update file
def addNewData():
    try:
        print("Add a new Person's data in the dictionary")
        key = raw_input("Enter the key that you want to enter in the dictionary : ")
        while key.isdigit():
            print("Enter the name for the key value which is string not an integer!!!")
            key = raw_input("Enter the key that you want to enter in the dictionary : ")

        value = raw_input("Enter the value you want to enter in the dictionary : ")
        k = 0
        while k == 0:
            try:
                int(value)
                k = 1
            except Exception:
                value = raw_input("Enter numeric digits only for value input: ")

            if k == 1:
                if (int(value) < 1000 or int(value) > 9999):
                    print("Enter the person's Id in the correct format - 4 digits!!!")
                    value = raw_input("Enter the value you want to enter in the dictionary : ")
                    k = 0
        nameid_d = readDataForAllFuncs()
        nameid_d[key] = value
        print(nameid_d)
        writeDataForAllFuncs(nameid_d)
    except Exception:
        print("Exception Occurred!!!")


# This function will be used to change the existing value from the dictionary and then update the text file
def modifyExistingValues():
    try:
        print("Change the existing values in the dictionary")
        print("The dictionary file is :")
        nameid_d = readDataForAllFuncs()
        print(nameid_d)
        key = raw_input("Enter the key for which you want to update the person's Id : ")
        k = 0
        while k == 0:
            if key in nameid_d:
                value = raw_input("Enter the value you want to enter in the dictionary : ")
                k = 1
            else:
                print("The key is not present in the dictionary!!!")
                options()

        if k == 1:
            m = 0
            while m == 0:
                try:
                    int(value)
                    m = 1
                except Exception:
                    value = raw_input("Enter numeric digits only for value input: ")

                if m == 1:
                    if (int(value) < 1000 or int(value) > 9999):
                        print("Enter the person's Id in the correct format - 4 digits!!!")
                        value = raw_input("Enter the value you want to enter in the dictionary : ")
                        m = 0

        nameid_d = readDataForAllFuncs()
        nameid_d[key] = value
        print(nameid_d)
        writeDataForAllFuncs(nameid_d)

    except Exception:
        print("Exception Occurred!!!")


# This function will be used to delete the existing value from the dictionary and then update the text file
def deletingValues():
    try:
        print("Delete the existing values in the dictionary")
        print("The dictionary file is:")
        nameid_d = readDataForAllFuncs()
        print(nameid_d)
        key = raw_input("Enter the key for which you want to delete the record : ")
        while key.isdigit():
            print("Enter the correct string and not the numbers!!!")
            key = raw_input("Enter the key for which you want to delete the record : ")

        if key in nameid_d:
            del nameid_d[key]
        else:
            print("The key is not present in the dictionary!!!")

        print(nameid_d)
        writeDataForAllFuncs(nameid_d)
    except Exception:
        print("Exception Occurred!!!")


# This function will give the details of the options to be performed on the dictionary file
def options():
    try:

        option = input(
            "Enter the option you want to perform:\n 1:Lookup for a person's Id number \n "
            "2: Add new name and person's Id\n 3:Change existing Personal Id \n "
            "4: Delete existing name and Personal Id \n 5:Exit\n")
        option = int(option)

        while option < 5:

            if option == 1:
                read_file()
            elif option == 2:
                addNewData()
            elif option == 3:
                modifyExistingValues()
            elif option == 4:
                deletingValues()
            else:
                sys.exit()
            option = input(
                "Enter the option you want to perform:\n 1:Lookup for an person's Id number \n 2: Add new name and "
                "personal Id \n 3:Change existing Personal Id \n 4: Delete existing name and Personal Id \n 5:Exit\n")
            option = int(option)
    except Exception:
        print("Exception Occurred!!!")


# Main function where program starts execution as per user's input
def main():
    try:
        write_file()
        options()
        sys.exit()
    except Exception:
        print("Exception Occurred!!!")

# Calling the main function
try:
    main()
except Exception:
    print("Exception Occurred!!!")
