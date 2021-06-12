# Very basic window.  Return values as a list
import threading

import PySimpleGUI as sg

from main.run import run_graphing_and_kml_process
from main.validation_handling import validate_google_sample_number

layout = [
    [sg.Text('First batch of locations to process: ')],
    [sg.InputText('', size=(60, 1), key='first_file_location'), sg.FileBrowse()],
    [sg.Text('Second batch of locations to process: ')],
    [sg.InputText('', size=(60, 1), key='second_file_location'), sg.FileBrowse()],
    [sg.Text('Units of height: '), sg.Combo(['Metres', 'Feet'], key='height_units', default_value='Metres'),
     sg.Text('Units of distance: '), sg.Combo(['Nautical miles', 'Miles', 'Kilometres'], key='distance_units',
                                              default_value='Nautical miles')],
    [sg.Text('Select and output folder: ')],
    [sg.InputText('', size=(60, 1), key='folder_output'), sg.FolderBrowse()],
    [sg.Text('Google elevation api key: ')],
    [sg.InputText('', size=(60, 1), key='api_key')],
    [sg.Text('How many samples between points?: ')],
    [sg.InputText('', size=(60, 1), key='samples')],
    [sg.Button('Run')],
    [sg.Output(size=(80, 10))]
]

window = sg.Window('Azimuth').Layout(layout)


# This method requires all fields to be completed and runs the google api graphing process only.
def run_application():
    first_file = values['first_file_location']
    second_file = values['second_file_location']
    height_units = values['height_units']
    distance_units = values['distance_units']
    output_folder = values['folder_output']
    api = values['api_key']
    amount_samples = int(values['samples'])
    validate_google_sample_number(amount_samples)
    run_graphing_and_kml_process(first_file, second_file, height_units, distance_units, output_folder, api,
                                 amount_samples)


while True:
    event, values = window.Read()
    if event is None or event == 'Exit':
        break
    if event == 'Run':
        x = threading.Thread(target=run_application(), daemon=True).start()
    if event is None:
        break
window.Close()
