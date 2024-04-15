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
