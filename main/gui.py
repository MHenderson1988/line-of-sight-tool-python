# Very basic window.  Return values as a list

if __name__ == "__main__":

    import PySimpleGUI as sg
    import threading
    from main.run import run_program

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
        [sg.Text('Select and output folder: ')],
        [sg.InputText('', size=(60, 1), key='folder_output'), sg.FolderBrowse()],
        [sg.Text('Generate .kml file'), sg.CBox('', key='kml_checkbox'),
         sg.Text('Download elevation data'), sg.CBox('', key='elevation_checkbox')],
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


    # This method determines if the checkbox is ticked
    def get_kml_checkbox():
        if values['kml_checkbox']:
            return "kml_true"
        else:
            return "kml_false"

    # This method determines if the user wishes to download elevation data to be used for graphing
    def get_elevation_checkbox():
        if values['elevation_checkbox']:
            return "elevation_true"
        else:
            return "elevation_false"


    # This method gathers the values from the GUI fields and passes them to the script which runs the program

    def thread_function_generate():
        first_file = values['first_file_location']
        first_file_type = get_radio_1()
        second_file = values['second_file_location']
        second_file_type = get_radio_2()
        output_folder = values['folder_output']
        generate_kml = get_kml_checkbox()
        api = values['api_key']
        amount_samples = int(values['samples'])
        run_program(first_file, second_file, output_folder, generate_kml,
                    api, amount_samples, first_file_type, second_file_type)


    while True:
        event, values = window.Read()
        if event is None or event == 'Exit':
            break
        if event == 'Run':
            x = threading.Thread(target=thread_function_generate)
            x.start()
        if event is None:
            break
    window.Close()
