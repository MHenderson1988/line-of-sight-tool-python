# Very basic window.  Return values as a list
from main.run import run_program

if __name__ == "__main__":

    import PySimpleGUI as sg
    import threading

    layout = [
        [sg.Text('First batch of locations to process: ')],
        [sg.InputText('', size=(60, 1), key='first_file_location'), sg.FileBrowse()],
        [sg.Radio('Decimal latitude-longitude', "first_file_type", default=True, size=(20, 1)),
         sg.Radio('Eastings-Northings (X,Y)', "first_file_type", size=(20, 1)),
         sg.Radio('OS Grid Reference', "first_file_type", size=(20, 1))],
        [sg.Text('Second batch of locations to process: ')],
        [sg.InputText('', size=(60, 1), key='second_file_location'), sg.FileBrowse()],
        [sg.Radio('Decimal latitude-longitude', "second_file_type", default=True, size=(20, 1)),
         sg.Radio('Eastings-Northings (X,Y)', "second_file_type", size=(20, 1)),
         sg.Radio('OS Grid Reference', "second_file_type", size=(20, 1))],
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


    def thread_function_generate():
        first_file = values['first_file_location']
        first_file_type = values['first_file_type']
        second_file = values['second_file_location']
        second_file_type = values['second_file_type']
        output_folder = values['folder_output']
        api = values['api_key']
        amount_samples = int(values['samples'])
        print(first_file, second_file, output_folder, api, amount_samples)
        run_program(first_file, second_file, output_folder, api, amount_samples)


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
