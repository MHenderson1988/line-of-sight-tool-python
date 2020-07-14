# Very basic window.  Return values as a list
import threading

import PySimpleGUI as sg

from main.run import run_graphing_and_kml_process
from main.validation_handling import validate_google_sample_number

layout = [
    [sg.Text('First batch of locations to process: ')],
    [sg.InputText('', size=(60, 1), key='first_file_location'), sg.FileBrowse()],
    [sg.Radio('Decimal latitude-longitude', "first_file_type", key='decimal_1', default=True, size=(20, 1)),
     sg.Radio('Eastings-Northings (X,Y)', "first_file_type", key='xy_1', size=(20, 1)),
     sg.Radio('OS Grid Reference', "first_file_type", key='bng_1', size=(20, 1))],
    [sg.Text('Second batch of locations to process: ')],
    [sg.InputText('', size=(60, 1), key='second_file_location'), sg.FileBrowse()],
    [sg.Radio('Decimal latitude-longitude', "second_file_type", key='decimal_2', default=True, size=(20, 1)),
     sg.Radio('Eastings-Northings (X,Y)', "second_file_type", key='xy_2', size=(20, 1)),
     sg.Radio('OS Grid Reference', "second_file_type", key='bng_2', size=(20, 1))],
    [sg.Text('Units of height: '), sg.Combo(['Metres', 'Feet'], key='height_units', default_value='Metres'),
     sg.Text('Units of distance: '), sg.Combo(['Nautical miles', 'Miles', 'Kilometres'], key='distance_units')],
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


# This method confirms the user's declared coordinate data type for the first locations .csv file and returns
# a string which will be used to select the appropriate conversion script.
def get_radio_1():
    if values['decimal_1']:
        return "decimal"
    if values['xy_1']:
        return "xy"
    if values['bng_1']:
        return "bng"


# This method confirms the user's declared coordinate data type for the first locations .csv file and returns
# a string which will be used to select the appropriate conversion script.

def get_radio_2():
    if values['decimal_2']:
        return "decimal"
    if values['xy_2']:
        return "xy"
    if values['bng_2']:
        return "bng"


# This method requires all fields to be completed and runs the google api graphing process only.
def run_application():
    first_file = values['first_file_location']
    first_file_type = get_radio_1()
    second_file = values['second_file_location']
    second_file_type = get_radio_2()
    height_units = values['height_units']
    distance_units = values['distance_units']
    output_folder = values['folder_output']
    api = values['api_key']
    amount_samples = int(values['samples'])
    validate_google_sample_number(amount_samples)
    run_graphing_and_kml_process(first_file, first_file_type, second_file, second_file_type, height_units,
                                 distance_units, output_folder, api, amount_samples)


while True:
    event, values = window.Read()
    if event is None or event == 'Exit':
        break
    if event == 'Run':
        x = threading.Thread(target=run_application())
        x.start()
    if event is None:
        break
window.Close()
