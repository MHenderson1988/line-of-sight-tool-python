# Very basic window.  Return values as a list
if __name__ == "__main__":

    import PySimpleGUI as sg
    import threading
    from getheight import generate_elevation
    from gridconverter import *
    from kmlgenerator import generatekml

    layout = [
              [sg.Text('Please select the location of the windfarm file to process: ')],
              [sg.InputText('', size=(30,1),key='fileLocation'), sg.FileBrowse()],
              [sg.Text('Are the coordinates in Northings and Eastings or OSGrid/WGS84 (Latitude/Longitude)?: ')],
              [sg.Radio('Northings and Eastings', 'Radio1', key='xy', default='True'), sg.Radio('OSGrid/WGS84','Radio1',key='wgs')],
              [sg.Text('Select folder to output .kml and elevation profiles: ')],
              [sg.InputText('', size=(30,1),key='folderoutput'), sg.FolderBrowse()],              
              [sg.Text('Step 1: Convert grids to a readable Lat/Long format (WGS84)', size=(50, 1)), sg.Button('Convert')],
              [sg.Text('Step 2: Create a Google Earth Pro .kml file (Optional)', size=(50, 1)), sg.Button('Create')],
              [sg.Text('Step 3: Generate line of sight assessment graphs', size=(50, 1)), sg.Button('Generate')],
              [sg.Output(size=(80, 10))]
             ]

    window = sg.Window('Prestwick Azimuth').Layout(layout)
    
    def thread_function_generate():
        output = values['folderoutput']
        generate_elevation(output)

    while True:
        event, values = window.Read()
        if event is None or event == 'Exit':
            break
        if event == 'Convert':
            file = values['fileLocation']
            if values['xy'] == True:
                convertgridsxy(file)
            else:
                convertgrids(file)
        if event == 'Create':
            output = values['folderoutput']
            generatekml(output)
        if event == 'Generate':
            x = threading.Thread(target=thread_function_generate)
            x.start()
        if event is None:
            break
    window.Close()