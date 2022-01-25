# Import
import  PySimpleGUI as sg


def create(data_array, headers):
    layout = [
        [sg.Table(values=data_array, headings=headers,
                  auto_size_columns=True,
                  display_row_numbers=True,
                  justification='right',
                  num_rows=20,
                  key='-TABLE-',
                  tooltip='VAS Table',
                  )]
    ]

    window = sg.Window("Scanned VAS Entries - Current Session",
                                           layout, modal=True, resizable=True)

    while True:
        event, values = window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break

    window.close()