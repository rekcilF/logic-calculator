# & C:/Users/Carlo/AppData/Local/Programs/Python/Python312/python.exe "d:/Admin Files/Desktop/digitec/table/test.py" 
import re

x = input("formula here: ")

y = []

listTruth = []

noOfVar = 0

def And(x, y):
    return x and y
def Or(x,y):
    return x or y

def checker(string):
    newString = string.replace("^", "").replace("|", "").replace(";", "").replace(">", "").replace("_", "")
    checkString = len(re.findall('/^[A-Za-z]$/', newString))
    if checkString > 0:
        print("bad letters used try again")
        exit()


def parser(string):
    i = 0
    while i != len(string):
        if "~" in string[i]:
            y.append(x[i] + x[i + 1])
            i += 1
        elif " " in string[i]:
            pass
        else:
            y.append(x[i])
        i += 1

def truthVar(list):

    global noOfVar
    for i in range(0, len(y)):
        noOfVar += len(re.findall('[A-Za-z]', y[i]))

def truth(vars, list):
    global noOfVar, listTruth

    x = 0
    y = noOfVar
    i = 0
    divisor = 2
    while x != noOfVar:

        totalNumber = 2**noOfVar
        repeatNumber = 0
        while (repeatNumber != (totalNumber/divisor)):
            if "~" in list[i][0]:
                listTruth.append(False)
            else:
                listTruth.append(True)
            repeatNumber += 1
        repeatNumber = 0
        while (repeatNumber != (totalNumber/divisor)):
            if "~" in list[i][0]:
                listTruth.append(True)
            else:
                listTruth.append(False)
            repeatNumber += 1
        x += 1
        divisor *= 2
    listTruth.append(True)
    listTruth.append(False)
    listTruth.reverse()

def operator(list, table):

    newTable = []
    for i in range(0, len(table)):
        newTable.append(table[i])
    print(len(newTable))
    results = []
    entry = 0
    entryString = 0
    operand = 0
    iter = 1
    if len(list) <= 2:
        print("too little arguments")
    
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
            newTable.pop(2**iter)
            newTable.pop(i)
            newTable.insert(i, answer)
            results.insert(0, answer)
        list.pop(0)
        list.pop(0)
    
    print(newTable, "answers table")
    print(len(newTable), "to", (len(table)//2))

checker(x)
parser(x)
print(y)
truthVar(y)
print(noOfVar)
truth(noOfVar, y)
print(listTruth)
operator(y, listTruth)