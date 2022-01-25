import PySimpleGUI as sg
import create_table
from user_login import user_input
from datetime import datetime

def check_ql_index(ql, data_array): #function to check index of scanned QL that is stored in nested list
    for outer_index, outer_value in enumerate(data_array):
        for inner_index, inner_value in enumerate(outer_value):
            if inner_value == ql:
                return (outer_index, inner_index)

user_input

data_array = []
headers = ['User', 'Shift', 'QL(UID)', 'DateTimeStart', 'DateTimeEnd', 'RecordCreation']

#Layout definition
layout = [
          [sg.Text('User:'), sg.Text(user_input['-USER-'])],
          [sg.Text('Shift:'), sg.Text(user_input['-SHIFT-'])],
          [sg.Text('Scan QL(UID):'), sg.Input(key='-QL(UID)-')],
          [sg.Button('Start Process'), sg.Button('End Process'), sg.Button('Show Table'), sg.Exit()]
         ]

# Create window
window = sg.Window('VAS Registration', layout, finalize=True)
window.bind('<Escape>', '-ESCAPE-') #bind ESC key to exit the code

# Event Loop
while True:
    event, values = window.read()
    if event in (None, 'Cancel', '-ESCAPE-', 'Exit'):
        break
    elif event == 'Start Process':
        start_datetime = datetime.now()
        data = [user_input['-USER-'], user_input['-SHIFT-'], values['-QL(UID)-'], start_datetime.strftime("%d.%m.%Y %H:%M:%S"), start_datetime.strftime("%d.%m.%Y %H:%M:%S"), start_datetime.strftime("%d.%m.%Y %H:%M:%S")]
        data_array.append(data)
        sg.Popup('Process Started')
    elif event == 'End Process':
        end_datetime = datetime.now()
        ql_outer_index, _ = check_ql_index(values['-QL(UID)-'], data_array)
        data_array[ql_outer_index][4] = end_datetime.strftime("%d.%m.%Y %H:%M:%S")
        sg.Popup('Process Ended')
        print(data_array)
    elif event == 'Show Table':
        create_table.create(data_array, headers)





