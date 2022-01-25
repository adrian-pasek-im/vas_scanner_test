# The import
import PySimpleGUI as sg

# Set the theme
#sg.theme('DarkGrey3')

# Layout definition
layout = [
          [sg.Text( 'User'), sg.Input(key='-USER-')],
          [sg.Text( 'Shift'), sg.Input(key='-SHIFT-')],
          [sg.Button('OK', bind_return_key=True), sg.Button('Cancel')] # bind_return_key - make pressing ENTER available
         ]

# Create window
window = sg.Window('VAS Registration', layout, finalize=True)
window.bind('<Escape>', '-ESCAPE-') #bind ESC key to exit the code

# Event Loop
while True:
    event, values = window.read()
    if event in (None, 'Cancel', '-ESCAPE-'):
        break
    if not values['-USER-'] in (None, '') and not values['-SHIFT-'] in (None, ''): #check if user and shift was entered, if not continue loop
        try:
            values['-SHIFT-'] = int(values['-SHIFT-'])
        except:
            sg.popup('Shift was detected to be a text. Please enter a number.', auto_close=True,)
            continue
        if not values['-SHIFT-'] in (1, 2, 3):
            sg.popup('Please type correct shift (1, 2, 3)', auto_close=True)
            continue
        user_input = values #save dict to use later
        sg.popup_no_buttons(f'USER: {user_input["-USER-"]}   SHIFT:{user_input["-SHIFT-"]}\n\nSession has started', auto_close=True, no_titlebar=True)
        break
    else:
        sg.popup('Please enter user and shift!')
        continue
# Close windows
window.close()