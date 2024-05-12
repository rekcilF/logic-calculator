# & C:/Users/Carlo/AppData/Local/Programs/Python/Python312/python.exe "d:/Admin Files/Desktop/digitec/table/table.py"
import PySimpleGUI as sg
import re
import os
import traceback
from ctypes import windll
windll.shcore.SetProcessDpiAwareness(1)

#styling fonting and the such
font = ('Calibri', 16, 'bold')
font2 = ('Calibri', 10, 'bold')
text = {'font':font, 'text_color':'#000000', 'background_color':'#FFFFFF'}
infoText = {'font':font2, 'text_color':'#000000', 'background_color':'#FFFFFF'}
infoText2 = {'font': ('Calibri', 10, 'bold'), 'text_color': '#000000', 'background_color':'#FFFFFF'}
convertBtn = {'font': font, 'size': (12, 1)}



# layout
layout = [
    [sg.Text('Truth Table Generator', **text, justification='center')],
    [sg.Text("Available Operators:\n^ = and \n| = or\n; = nand\n> = nor\n_ = xor\n~ to indicate negation\nfor example: ~a^b", **infoText)],
    [sg.Input('~a^b', key='input', enable_events=True, size=(40,100))],
    [sg.Text('', key='error', **infoText)],
    [sg.Button('Calculate', key='calc', **convertBtn, button_color="#007AFF")]
]

# hilarious functions and such

# defines different propositional logic operators as functions (And, Or, not And (nand), not Or (nor), exclusive or (xor))

def And(x, y):
    c = x and y
    return c
    # returns the variable in the function as a variable that can be used outside the function
def Or(x,y):
    c = x or y
    return c
def Nand(x, y):
    c = not (x and y)
    return c
def Nor(x, y):
    c = not (x or y)
    return c
def Xor(x, y):
    c = x ^ y
    return c

# function removes all of the spaces in a string

def removeSpace(string):
    try:
        newString = string.replace(" ", "")
        return newString
        # replaces whitespace with empty space
    except Exception as e:
        raise Exception("Error!!")

        # try except block tries to execute a piece of code and if there is an error, it doesn't crash the program and instead executes the code in the except block

# function that checks a string for forbidden characters which is every character except for the allowed operators and A-z

def checker(string):
    try:
        newString = string.replace("^", "").replace("|", "").replace(";", "").replace(">", "").replace("_", "").replace("~", "")
        # creates a new string based off an input and replaces the operators with empty space
        checkString = len(re.findall('[^A-Za-z]', newString))
        if checkString > 0:
            raise Exception("Prohibited characters used, use only letters and operators!")
            # len(re.findall()) turns re.findall into a number which is the amount of times re.findall has been found

            # if statement used to check if there is any instance of forbidden letters, it notifies the user that prohibited letters was used and indicates the error
    except Exception as e:
        raise Exception(e)

# function that creates a table and separates a string into variables and operators

def parser(string):
    try:
        # global variables declared as variables are used in for loops and while loops in the function
        global countOperators, expectedOperators
        table = []
        # declaration of a list
        i = 0
        try:
            table = re.split(r"([\>|\_|\;|\||\^])", string)
            if table[(len(table) - 1)] == '':
                table.pop((len(table) - 1))
            # splits a string via a separator using regex whcih finds instances of operator characters then separates them into variables and into operators
            countOperators = 0
            expectedOperators = int(((len(table) + 1) / 2) - 1)
            counter = 0
            while counter != len(table):
                if table[counter] == '':
                    table.pop(counter)
                counter += 1
            for x in range(0, len(table)):
                countOperators += len(re.findall(r"[\>|\_|\;|\||\^]", table[x]))
            # for loop which repeats for every number in the range between 0 and the length of table
            if re.findall(r"[\>|\_|\;|\||\^]", table[0]):
                raise Exception("Can't start with operator!")
            if (len(table) % 2) != 1:
                raise Exception("Too many variables or operators!")
            if countOperators != expectedOperators:
                raise Exception("Too many variables!")
            # find all used to identify the operator in conjunction with an if statement which checks if the first character begins with an operator and exits if it is true
        except Exception as e:
            raise Exception(e)
        return table

        # returns a list of a parsed string as a variable
    except Exception as e:
        raise Exception(e)

# function that returns a list with only variables and the number of varibles

def truthVar(list):
    try:
        x = 0
        newList = []
        for i in range(0, len(list)):


            if len(re.findall('[A-Za-z]', list[i])):
                newList.append(list[i])
                x += 1
                # += used to keep track of all instances of A-z when iterating through a list
        return x, newList
    except Exception as e:
        raise Exception("Error in variables!")

def repeatChecker(list):
    try:
        for x in range(len(list)):
            tildaChecker = len(re.findall('~', list[x]))
            if tildaChecker > 1:
                raise Exception("Only negate once!")
            y = 0

            if tildaChecker == 1 and list[x][0] != "~":
                raise Exception("Negation only goes at the start of the variable!")
    except Exception as e:
        raise Exception(e)

def duplicateChecker(list):
    try:
        for x in range(len(list)):
            y = 0
            while y != (len(list) - (x + 1)):
                z = x + 1
                if list[x] == list[y+z]:
                    raise Exception("Duplicate variables detected!")
                y += 1
    except Exception as e:
        raise Exception(e)

# function that creates a complete truth table with every combination of true and false between all the variables

def truth(vars, list):
    try:
        newList = []
        otherList = []
        for i in range(0, len(list)):
            newList.append(list[i])
            otherList.append(list[i])
        x = 0
        y = vars
        listTruth = []
        listTruthTable = []
        divisor = 2
        i = 0
        count = 0
        while i != len(list):
            if len(re.findall(r"[\>|\_|\;|\||\^]", otherList[count])):
                newList.pop(count)
                otherList.pop(count)
                count -= 1
                # list.pop(int) function removes an entry from the list in the location of int e.g [1, 2, 3], list.pop(2) removes the 3 from the list
            i += 1
            count += 1
        while x != y:

            totalNumber = 2**y
            # exponential
            repeatNumber = 0
            while (repeatNumber != (totalNumber/divisor)):
                if "~" in newList[x][0]:
                    listTruth.append(False)
                    listTruthTable.append(False)
                else:
                    listTruth.append(True)
                    listTruthTable.append(True)
                repeatNumber += 1
            repeatNumber = 0
            while (repeatNumber != (totalNumber/divisor)):
                if "~" in newList[x][0]:
                    listTruth.append(True)
                    listTruthTable.append(True)
                else:
                    listTruth.append(False)
                    listTruthTable.append(False)

                repeatNumber += 1
            x += 1
            divisor *= 2
        listTruth.append(True)
        listTruth.append(False)
        listTruth.reverse()
        listTruthTable.reverse()
        # list.reverse() reverses the list from back to front
        return listTruth, listTruthTable
        # returns two values as a list e.g [[listTruth], [listTruthTable]] and can be referred to as varName = truth(vars, list)[0] or varName = truth(vars, list)[1]
    except Exception as e:
        raise Exception("You shouldn't see this error - error in truth table generator!")

# function that takes a parsed list and the associated truth table with it and executes the propositional logic (and, or, xor, nor and nand) and returns a complete table with all the results

def operator(list, table):
    try:
        newTable = []
        for i in range(0, len(table)):
            newTable.append(table[i])
        results = []
        iter = 1
        if len(list) <= 2:
            raise Exception("Not enough variables!")
        try:
            while len(list) != 1:
                lengthRequired = len(table)
                extra = len(results) % (2**iter)
                while extra != 0:
                    results.pop()
                    extra = len(results) % (2**iter)

                if newTable != lengthRequired:
                    for i in range(0, len(results)):
                        newTable.insert(0, results[i])
                iter += 1
                total = len(newTable)
                repeat = total//8
                for i in range(0, 2**iter):
                    if list[1] == "^":
                        answer = And(newTable[i], newTable[2**iter])
                    elif list[1] == '|':
                        answer = Or(newTable[i], newTable[2**iter])
                    elif list[1] == ';':
                        answer = Nand(newTable[i], newTable[2**iter])
                    elif list[1] == '>':
                        answer = Nor(newTable[i], newTable[2**iter])
                    elif list[1] == "_":
                        answer = Xor(newTable[i], newTable[2**iter])
                    else:
                        raise Exception("Thats not an operator!")
                    # elif meaning else if which allows an if statement to be chained with other if statements
                    # else which means at the end of the if else statement, if none of those are met, the code in the else block is ran
                    newTable.pop(2**iter)
                    newTable.pop(i)
                    newTable.insert(i, answer)
                    results.insert(0, answer)

                    # list.insert(pos, value) which inserts (value) into the list at the position (pos)
                list.pop(0)
                list.pop(0)
        except Exception as e:
            raise Exception("Calculator Error!")

        return newTable
    except Exception as e:
        raise Exception(e)

# function that takes the completed truth table and the number of variables and correctly split the completed truth table and associate them with a variable

def lister(table, noOfVar):
    try:
        listTable = []
        for p in range(0, len(table)):
            listTable.append(table[p])
        newList = []
        x = 0
        max = -1
        start = -1
        for p in range(0, noOfVar):
            thing = (((2 ** noOfVar) // (2 ** x)) // 2)
            start += 2**x
            max += (2**(x+1))
            for z in range(0, thing):
                for x in range(start,(max+1)):
                    newList.append(listTable[x])
            x = p + 1
        newTable = []
        for i in range(0, len(newList), (len(newList)//noOfVar)):
            newTable.append(newList[i:i + (len(newList) // noOfVar)])
            # // is floor division, division as a whole number even if there are decimals in the answer
            # for loop increments based on 3 variables
        return newTable
    except Exception as e:
        raise Exception("Unknown Error - you shouldn't see this...")

def operatorOnly(list):

    try:
        opList = []
        for x in range(0, len(list)):
            if len(re.findall(r"[\>|\_|\;|\||\^]", list[x])):
                opList.append(list[x])

        opList.append("=")
        return opList
    except Exception as e:
        raise Exception(e)

def addOperator(varList, opList):
    try:
        newList = []
        for x in range(0, (len(varList))):
            newList.append(varList[x])
        counter = 0
        for x in range(0, len(opList)):
            counter += 1
            newList.insert((x + counter), opList[x])
        return newList
    except Exception as e:
        raise Exception(e)

def listToString(list):
    try:
        newList = []
        for x in range(0, len(list)):
            newList.append(list[x])
        string = str(newList)
        newString = string.replace("^", "and").replace("|", "or").replace(';', 'nand').replace(">", 'nor').replace("_", "xor").replace('[', '').replace(']', '').replace(',', '').replace('\'', '')
        return newString
    except Exception as e:
        raise Exception(e)
# split a list into different character sizes
def splitter(list, noOfEnt):
    return [list[x : x + noOfEnt] for x in range(0, len(list), noOfEnt)]

# creates a new list that counts every 1st character in all lists because pysimplegui reads vertically not horizontally (very stinky)

def skipper(list):
    amtList = len(list)
    amtInList = len(list[0])
    newList = []
    x = 0
    while x != (amtInList):
        for y in range(0, amtList):
            newList.append(list[y][x])
        x += 1
    return newList

# function that simplifies the calculating process into one function that takes a string and returns both the results and the completed truth table

def calculator(x):
    try:
        x = removeSpace(x)
        checker(x)
        y = parser(x)
        repeatChecker(y)
        noOfVar = truthVar(y)[0]
        vars = truthVar(y)[1]
        duplicateChecker(vars)
        listTruth = truth(noOfVar, y)[0]
        listTable = truth(noOfVar, y)[1]
        results = operator(y, listTruth)
        table = lister(listTable, noOfVar)
        psgTable = lister(listTable, noOfVar)
        psgHeader = []
        for i in range(0, noOfVar):
            psgHeader.append(vars[i])
        psgHeader.append(x)
        psgTable.append(results)
        opOnly = operatorOnly(parser(x))
        psgTable1 = skipper(psgTable)
        psgTable2 = splitter(psgTable1, (len(psgTable1)//(len(psgTable1)//(noOfVar + 1))))
        return results, table, psgTable2, psgHeader, noOfVar, opOnly
    except Exception as e:
        message = 136
        return message, e

# popup Window

def tableWindow(x, y, z):
    lengthOfRows = len(x)
    scroll = 'Click on the row to see the equation'
    scrollToggle = True
    font3 = ('Calibri', 9)
    closeText = {'font':font3, 'text_color':'#000000', 'background_color':'#FFFFFF'}
    if lengthOfRows > 32:
        lengthOfRows = 32
        scroll = 'Click on the row to see the equation \nScroll to see the full truth table'
        scrollToggle = False

    layout = [
        [sg.Text(scroll, **infoText)],
        [sg.Table(x, headings=y, **infoText, auto_size_columns=False, hide_vertical_scroll=scrollToggle, num_rows=lengthOfRows, sbar_width = 8, sbar_arrow_width = 2, enable_events = True, enable_click_events = True)],
        [sg.Text('', key='display', **infoText)],
        [sg.Text('All equations are calculated left to right', **infoText)],
        [sg.Text('Close this window to return to the main window', **closeText)]
    ]

    newWindow = sg.Window("Truth Table View", layout, background_color="#FFFFFF", grab_anywhere=True, modal=True)
    while True:
        event, value = newWindow.read()
        if event == 0:
            complete = addOperator(x[value[0][0]], z)
            completeString = listToString(complete)
            newWindow['display'].update(value=('Selected equation: '+completeString))
        if event == sg.WIN_CLOSED:
            break

    newWindow.close()

# main window


window = sg.Window('Truth Table Generator', layout, background_color="#FFFFFF", grab_anywhere=True, finalize=True)

while True:

    event, value = window.read()

    string = value['input']
    if event == "calc":
        if calculator(string)[0] == 136:
            window['error'].update(value=calculator(string)[1])
        else:
            window['error'].update(value='')
            psgTable = calculator(string)[2]
            psgHeader = calculator(string)[3]
            vars = calculator(string)[4] + 1
            psgTable1 = skipper(psgTable)
            psgTable2 = splitter(psgTable1, (len(psgTable1)//(len(psgTable1)//vars)))

            opVar = calculator(string)[5]

            tableWindow(psgTable, psgHeader, opVar)

    if event == sg.WIN_CLOSED:
        break


window.close()
