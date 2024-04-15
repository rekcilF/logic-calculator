# & C:/Users/Carlo/AppData/Local/Programs/Python/Python312/python.exe "d:/Admin Files/Desktop/digitec/table/table.py"
import PySimpleGUI as sg
import re
import os
import traceback

#styling fonting and the such
font = ('Calibri', 13)
text = {'font':font, 'text_color':'#000000', 'background_color':'#FFFFFF'}
convertBtn = {'font': font, 'size': (10, 1)}

# layout
layout = [
    [sg.Text('trooth table', **text)],
    [sg.Input('0', key='input', enable_events=True)],
    [sg.Text('', key='error', **text)],
    [sg.Button('calculate', key='calc', **convertBtn)]
]

# hilarious functions and such

# defines different propositional logic operators as functions (And, Or, not And (nand), not Or (nor), exclusive or (xor))

def And(x, y):
    c = x and y
    return c

    # returns a variable as a variable
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
        print(e)

        # try except block tries to execute a piece of code and if there is an error, it doesn't crash the program and instead executes the code in the except block

# function that checks a string for forbidden characters which is every character except for the allowed operators and A-z

def checker(string):
    try:
        newString = string.replace("^", "").replace("|", "").replace(";", "").replace(">", "").replace("_", "").replace("~", "")
        # creates a new string based off an input and replaces the operators with empty space
        checkString = len(re.findall('[^A-Za-z]', newString))
        if checkString > 0:
            print("bad letters used try again")
            exit()
            # len(re.findall()) turns re.findall into a number which is the amount of times re.findall has been found

            # if statement used to check if there is any instance of forbidden letters, it notifies the user that bad letters were used and exits the program
    except Exception as e:
        print(e)

# function that creates a table and separates a string into variables and operators

def parser(string):
    try:
        # global variables declared as variables are used in for loops and while loops in the function
        global countOperators, expectedOperators
        table = []
        # declaration of a list
        i = 0
        try:
            while i != len(string):
                # while loop used which states that if i is not the same value as the length of the string, it will keep running the code in the loop
                if "~" in string[i]:
                    table.append(string[i] + string[i + 1])
                    i += 1
                    # append adds an entry into the end of the list
                else:
                    table.append(string[i])
                i += 1
            countOperators = 0
            expectedOperators = int(((len(table) + 1) / 2) - 1)
            for x in range(0, len(table)):
                countOperators += len(re.findall(r"[\>|\_|\;|\||\^]", table[x]))
            # for loop which repeats for every number in the range between 0 and the length of table
            if countOperators != expectedOperators:
                print("too many vars or operators")
                print("vars", len(table), "expected operators", expectedOperators, "actual operators", countOperators)
                exit()
            if re.findall(r"[\>|\_|\;|\||\^]", table[0]):
                print("can't start with operator")
                exit()
            # find all used to identify the operator in conjunction with an if statement which checks if the first character begins with an operator and exits if it is true
        except Exception as e:
            print("error in parser")
            print(e.message, e.args)
            exit()
        return table

        # returns a list of a parsed string as a variable
    except Exception as e:
        print(e)

# function that returns a list with only variables and the number of varibles

def truthVar(list):
    try:
        x = 0
        newList = []
        for i in range(0, len(list)):
            x += len(re.findall('[A-Za-z]', list[i]))

            # += used to keep track of all instances of A-z when iterating through a list
            if len(re.findall('[A-Za-z]', list[i])):
                newList.append(list[i])
        return x, newList
    except Exception as e:
        print(e)

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
        print(e)

# function that takes a parsed list and the associated truth table with it and executes the propositional logic (and, or, xor, nor and nand) and returns a complete table with all the results

def operator(list, table):
    try:
        newTable = []
        for i in range(0, len(table)):
            newTable.append(table[i])
        results = []
        iter = 1
        if len(list) <= 2:
            print("too little arguments")

        try:
            print(list)
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
                        print("thats not an operator!")
                        exit()
                    # elif meaning else if which allows an if statement to be chained with other if statements
                    # else which means at the end of the if else statement, if none of those are met, the code in else is ran
                    newTable.pop(2**iter)
                    newTable.pop(i)
                    newTable.insert(i, answer)
                    results.insert(0, answer)

                    # list.insert(pos, value) which inserts (value) into the list at the position (pos)
                list.pop(0)
                list.pop(0)
                print(list)
        except Exception as e:
            print("sumn bad happened")
            print(e, e.__cause__)
            exit()

        return newTable
    except Exception as e:
        print(e)

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
        print(e)

# function that simplifies the calculating process into one function that takes a string and returns both the results and the completed truth table

def calculator(x):
    try:
        x = removeSpace(x)
        checker(x)
        y = parser(x)
        noOfVar = truthVar(y)[0]
        vars = truthVar(y)[1]
        listTruth = truth(noOfVar, y)[0]
        listTable = truth(noOfVar, y)[1]
        results = operator(y, listTruth)
        table = lister(listTable, noOfVar)
        for i in range(0, noOfVar):
            print("var:", vars[i], table[i])
        print(x, results)
        print("entered formula:", x)
        return results, table
    except Exception as e:
        print(e)

# the input part

print(" ^ = and \n | = or\n ; = nand\n > = nor\n _ = xor\n ~ to indicate negation\nfor example ~a^b")

ans = input("formula here: ")
truthTable = calculator(ans)[0]
resultTable = calculator(ans)[1]

print(truthTable, resultTable)





# window


window = sg.Window('Propositional Logic Calculator', layout, background_color="#FFFFFF", grab_anywhere=True)

while True:
    event, value = window.read()
    print("Event", event)
    print("Value", value)

    while len(value['input']) > 5:
        value['input'] = ''
        window['error'].update(value='too many!')




    if event == sg.WIN_CLOSED:
        break

window.close()
