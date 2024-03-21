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
    newString = string.replace("^", "").replace("|", "").replace(";", "").replace(">", "").replace("_", "").replace("~", "").replace(" ", "")
    checkString = len(re.findall('[^A-Za-z]', newString))
    if checkString > 0:
        print("bad letters used try again")
        exit()


def parser(string):
    global countOperators, expectedOperators
    table = []
    i = 0
    try:
        while i != len(string):
            if "~" in string[i]:
                table.append(string[i] + string[i + 1])
                i += 1
            elif " " in string[i]:
                pass
            else:
                table.append(string[i])
            i += 1
        countOperators = 0
        expectedOperators = int(((len(table) + 1) / 2) - 1)
        for x in range(0, len(table)):
            countOperators += len(re.findall(r"[\>|\_|\;|\||\^]", table[x]))
        if countOperators != expectedOperators:
            print("too many vars or operators")
            print("vars", len(table), "expected operators", expectedOperators, "actual operators", countOperators)
            exit()
        if re.findall(r"[\>|\_|\;|\||\^]", table[0]):
            print("can't start with operator")
            exit()
    except Exception as e:
        print("error in parser")
        print(e.message, e.args)
        exit()
    return table

def truthVar(list):

    x = 0
    for i in range(0, len(y)):
        x += len(re.findall('[A-Za-z]', y[i]))
    return x


def truth(vars, list):
    newList = []
    otherList = []
    for i in range(0, len(list)):
        newList.append(list[i])
        otherList.append(list[i])
    print(newList, list)
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
        i += 1
        count += 1
    while x != y:

        totalNumber = 2**y
        repeatNumber = 0
        print(newList[x][0], "list")
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
    return listTruth, listTruthTable

def operator(list, table):

    newTable = []
    for i in range(0, len(table)):
        newTable.append(table[i])
    print(len(newTable))
    results = []
    iter = 1
    if len(list) <= 2:
        print("too little arguments")

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
                newTable.pop(2**iter)
                newTable.pop(i)
                newTable.insert(i, answer)
                results.insert(0, answer)
            list.pop(0)
            list.pop(0)
    except Exception as e:
        print("sumn bad happened")
        print(e, e.__cause__)
        exit()

    return newTable

def lister(table, noOfVar):
    print(len(table), noOfVar)
    listTable = []
    for p in range(0, len(table)):
        listTable.append(table[p])
    newList = []
    x = 0
    max = -1
    count = 1
    start = -1
    for p in range(0, noOfVar):
        thing = (((2 ** noOfVar) // (2 ** x)) // 2)
        print(thing, "thing")
        print(start,"before")
        start += 2**x
        print(start,"after")
        max += (2**(x+1))



        for z in range(0, thing):
            for x in range(start,(max+1)):
                newList.append(listTable[x])
                print("added", listTable[x], x)
            count += 1



        x = p + 1

    newTable = []
    for i in range(0, len(newList), (len(newList)//noOfVar)):
        newTable.append(newList[i:i + (len(newList) // noOfVar)])
    return newTable




checker(x)
y = parser(x)
print(y)
noOfVar = truthVar(y)
print(noOfVar, y)
listTruth = truth(noOfVar, y)[0]
listTable = truth(noOfVar, y)[1]
print(listTruth, y)
print(listTruth)
results = operator(y, listTruth)
print(results)
print(listTable, len(listTable))
table = lister(listTable, noOfVar)
print(table)

