'''
ITMD 513 : Assignment 5- Q2 - Bhanu kureti
Summary : This program will convert alphabetic phone number into Numeric
'''

# Create function to validate user's input
def userInput():
    alphaPhoneCode = ''
    keepLooping = True
    while keepLooping:
        alphaPhoneCode = str(input('\n Enter the 10 digit Alphabetic telephone number to be converted [as xxx-xxx-xxxx]: ').rstrip())
        alphaPhoneCode = alphaPhoneCode.upper()
        if len(alphaPhoneCode) == 12:
            if alphaPhoneCode[3] == '-' and alphaPhoneCode[7] == '-':
                keepLooping = False
            else:
                print('\n Alphabetic phone number should Contain \'-\' in 3rd and 7th index place. format should be in XXX-XXX-XXXX')
        elif len(alphaPhoneCode) < 12 and alphaPhoneCode[3] != '-' and alphaPhoneCode[7]!='-':
            print('Alphabetic phone number should contain 10 characters and should contain \'-\' symbols at 3rd and 7th index')
        else:
            print('Alphabetic phone number should not exceed 10 characters without hypen symbol')
    return alphaPhoneCode

# function to assign char values with desired number
def getNumForalpha(alphaChar):
    alphaNumValue = {
        'A': '2', 'B': '2', 'C': '2',
        'D': '3', 'E': '3', 'F': '3',
        'G': '4', 'H': '4', 'I': '4',
        'J': '5', 'K': '5', 'L': '5',
        'M': '6', 'N': '6', 'O': '6',
        'P': '7', 'Q': '7', 'R': '7', 'S': '7',
        'T': '8', 'U': '8', 'V': '8',
        'W': '9', 'X': '9', 'Y': '9', 'Z': '9'
    }
    return alphaNumValue[alphaChar]

# function to covert the alpha codes to numbers
def alphaToNumCovert(codeToConvert):
    convertedCode = ''
    for code in codeToConvert:
        if code.isalpha():
            numForCode = getNumForalpha(code)
            convertedCode += str(numForCode)
        else:
            convertedCode += str(code)

    return convertedCode

# function to print numeric telephone number
def displayTeleNum(f_3,m_3,l_4):
    Num = "{}-{}-{}".format(f_3, m_3, l_4)
    return Num

# Main function where execution starts
def main():
    # Validate user's input
    alphaNumUserCode = userInput()

    # Split the user's input to a list
    alphaNumCodeList = alphaNumUserCode.split('-')

    # Convert first three
    first_Three = alphaToNumCovert(alphaNumCodeList[0])

    # Convert middle three
    mid_Three = alphaToNumCovert(alphaNumCodeList[1])

    # Convert last four
    last_Four = alphaToNumCovert(alphaNumCodeList[2])

    # Display the converted Alphabetic Telephone Number
    convertTeleNum = displayTeleNum(first_Three, mid_Three, last_Four)
    print('Converted Numeric Telephone Number is: ', convertTeleNum)
# call Main function
main()



