# & C:/Users/Carlo/AppData/Local/Programs/Python/Python312/python.exe "d:/Admin Files/Desktop/digitec/table/table.py"
import PySimpleGUI as sg

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

font = ('Calibri', 13)
text = {'font':font, 'text_color':'#000000', 'background_color':'#FFFFFF'}
convertBtn = {'font': font, 'size': (10, 1)}


layout = [
    [sg.Text('trooth table', **text)],
    [sg.Input('0', key='input', enable_events=True)],
    [sg.Text('', key='error', **text)],
    [sg.Button('calculate', key='calc', **convertBtn)]
]

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