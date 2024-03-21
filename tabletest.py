# & C:/Users/Carlo/AppData/Local/Programs/Python/Python312/python.exe "d:/Admin Files/Desktop/digitec/table/tabletest.py" 
import re
import itertools



E = True
e = True
F = False
f = False
G = True
g = False
H = True
h = False
one = False
two = False
three = False
four = False



def negate(x, y):
    global E, F, G, H, e, f, g, h, one, two, three, four
    if (x == 1 and y == 1):
        E = False
        e = False
        F = True
        f = True
        G = False
        g = True
        H = False
        h = True
    elif (x == 1 and y == 0):
        E = False
        e = False
        F = True
        f = True
    elif (x == 0 and y == 1):
        G = False
        g = True
        H = False
        h = True
    elif (x == 0 and y == 0):
        one = False
        two = False
        three = True
        four = True
    else:
        print("error in x and y in negation")
        exit()


def And():
    global E, F, G, H, e, f, g, h, one, two, three, four
    one = E and G
    two = e and g
    three = F and H
    four = f and h
def Or():
    global E, F, G, H, e, f, g, h, one, two, three, four
    one = E or G
    two = e or g
    three = F or H
    four = f or h
def nand():
    global E, F, G, H, e, f, g, h, one, two, three, four
    one = not (E and G)
    two = not (e and g)
    three = not (F and H)
    four = not (f or h)


x = input("something ")
# if len(x) > 5:
#     print("no - too long")
#     exit()


try:
    y = re.split("[\^\>\;\!\_]", x)
except re.error:
    print("no - operator fail")
    exit()

a = re.search("\^", x)
b = re.search("\>", x)
c = re.search("\;", x)
d = re.search("\!", x)
p = re.search("\_", x)

if a:
    print("^")
    operator = 1
    # and
elif b:
    print(">")
    operator = 2 
    # or
elif c:
    print(";")
    operator = 3
    # nand
elif d:
    print("!")
    operator = 4
    # xor
elif p:
    # nor
    print("_")
    operator = 5

# if (len(y) > 2):
#     print("something bad happened, it got split more than once")
#     exit()

try:
    print(y)

    z = len(y)

    variables = dict()
    for i in range(0, len(y)):
        variables[y[i]] = True
        print(variables)
    
    for i in variables.keys():
        x = i.count("~")
        if x > 1:
            print("too many negations")
            exit()
    
    if len(variables) != 1:
        print("calculations here")
        answerList = []
        
        exit()



    # if len(y[0]) != 1 or len(y[1]) != 1:
    #     if "~" in y[0][0] and "~" in y[1][0]:
    #         print("negation on both vars")
    #         E = False
    #         e = False
    #         F = True
    #         f = True
    #         G = False
    #         g = True
    #         H = False
    #         h = True
    #     elif "~" in y[0][0]:
    #         print("negation on var one")
    #         E = False
    #         e = False
    #         F = True
    #         f = True
    #     elif "~" in y[0]:
    #         print("no negation wrong")
    #     elif "~" in y[1][0]:
    #         print("negation on var two")
    #         G = False
    #         g = True
    #         H = False
    #         h = False
    #     elif "~" in y[1]:
    #         print("wrong negation")
    if (operator == 1):
        And()
    if (operator == 2):
        Or()
    if (operator == 3):
        nand()
    # if (operator == 4):
    #     xor()
    # if (operator == 5):
    #     print(not (E or G))
    #     print(not (e or g))
    #     print(not (F or H))
    #     print(not (f or h))


except IndexError:
    if (len(y[0]) == 2):
        if ("~" in y[0][0]):
            print(not E)
            print(not e)
            print(not F)
            print(not f)
        else:
            print("no - negation error")
        exit()
    print("no - index error")

print(one, two, three, four)