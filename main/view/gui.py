# Very basic window.  Return values as a list
import os
import threading

import PySimpleGUI as sg

from main.classes.line_of_sight import LineOfSight
from main.db.db_logic import get_data_from_table


# This is the main window which will greet the user on first start up
def main():
    layout = [
        [sg.Table(values=get_data_from_table("name", table='projects'), headings=["Project name"])]
    ]

    window = sg.Window("Main window", layout)

    while True:
        event, values = window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break
        if event == 'new comparison':
            new_comparison_window()


# This window is for creating a new analysis between two sets of locations
def new_comparison_window():
    layout = [
        [sg.Text('First batch of locations to process: ')],
        [sg.InputText('', size=(60, 1), key='first_file_location'), sg.FileBrowse()],
        [sg.Text('Second batch of locations to process: ')],
        [sg.InputText('', size=(60, 1), key='second_file_location'), sg.FileBrowse()],
        [sg.Text('Units of height: '), sg.Combo(['METRES', 'FEET'], key='height_units', default_value='METRES'),
         sg.Text('Units of distance: '), sg.Combo(['NAUTICAL_MILES', 'MILES', 'KILOMETRES'], key='distance_units',
                                                  default_value='NAUTICAL_MILES')],
        [sg.Text('Select and output folder: ')],
        [sg.InputText('', size=(60, 1), key='folder_output'), sg.FolderBrowse()],
        [sg.Text('Google elevation api key: ')],
        [sg.InputText('', size=(60, 1), key='api_key')],
        [sg.Text('How many samples between points?: ')],
        [sg.InputText('', size=(60, 1), key='samples')],
        [sg.Button('Run')],
        [sg.Output(size=(80, 10))]
    ]
    window = sg.Window("Second window", layout, modal=True)

    # This method requires all fields to be completed and runs the google api graphing process only.
    def run_application():
        first_file = values['first_file_location']
        second_file = values['second_file_location']
        height_units = values['height_units']
        distance_units = values['distance_units']
        output_folder = values['folder_output']
        api = values['api_key']
        amount_samples = int(values['samples'])

        los = LineOfSight(first_file, second_file, samples=amount_samples, key=api, height_units=height_units,
                          distance_units=distance_units, output=output_folder)
        los.get_los()

    # Event loop
    while True:
        event, values = window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break
        if event == 'Run':
            x = threading.Thread(target=run_application(), daemon=True).start()

    window.close()


# Used to quickly find the database file
def create_db_file_path():
    CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(CURRENT_DIR, "../db/test.db")


if __name__ == '__main__':
    main()
