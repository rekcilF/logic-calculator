import re
import os
import traceback

print(" ^ = and \n | = or\n ; = nand\n > = nor\n _ = xor\n ~ to indicate negation\nfor example ~a^b")

def And(x, y):
    c = x and y
    return c
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

def removeSpace(string):
    try:
        newString = string.replace(" ", "")
        return newString
    except Exception as e:
        print(e)

def checker(string):
    try:
        newString = string.replace("^", "").replace("|", "").replace(";", "").replace(">", "").replace("_", "").replace("~", "")
        checkString = len(re.findall('[^A-Za-z]', newString))
        if checkString > 0:
            print("bad letters used try again")
            exit()
    except Exception as e:
        print(e)

def parser(string):
    try:
        global countOperators, expectedOperators, table
        table = []
        i = 0
        try:
            # while i != len(string):
            #     if "~" in string[i]:
            #
            #         table.append(string[i] + string[i + 1])
            #         i += 1
            #     else:
            #         table.append(string[i])
            #     i += 1
            table = re.split(r"([\>|\_|\;|\||\^])", string)
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
    except Exception as e:
        print(e)

def truthVar(list):
    try:
        x = 0
        newList = []
        for i in range(0, len(list)):
            if len(re.findall('[A-Za-z]', list[i])):
                newList.append(list[i])
                x += 1
        return x, newList
    except Exception as e:
        print(e)


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
            i += 1
            count += 1
        while x != y:

            totalNumber = 2**y
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
        return listTruth, listTruthTable
    except Exception as e:
        print(e)

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
                    newTable.pop(2**iter)
                    newTable.pop(i)
                    newTable.insert(i, answer)
                    results.insert(0, answer)
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
        return newTable
    except Exception as e:
        print(e)


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
    except Exception as e:
        print(e)

ans = input("formula here: ")
calculator(ans)

os.system("pause")
