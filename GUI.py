### This is a standalone app. Works on its own   ###
### To run this just run the .py in your terminal >> python3 GUI.py

import PySimpleGUI as sg
from pytube import YouTube


import pytube.request # for changing the default interval at which a progress bar is updated
# below is Progress bar update resolution. One progress bar per each chunk.
# smaller chunk size == chunk progression updated more frequently
# Change the value here to something smaller to decrease chunk sizes,
#  thus increasing the number of times that the progress callback occurs
pytube.request.default_range_size = 437184  # 9MB chunk size

# defining functions that allow for progress bar while downloading. Are called when YouTube video_object is called in main function
def progress_check(stream, chunk, bytes_remaining):
        window['-DOWNLOADPROGRESS-'].update(100 - round(bytes_remaining / stream.filesize * 100))

def on_complete(stream, file_path):
    window['-DOWNLOADPROGRESS-'].update(0)

# define the apps start layout variable that will be used to initialize the first window instance
start_layout = [
        [sg.Input(key = '-INPUT-'),sg.Button('submit')],
    ]

# define the content of main_layout first tab as info_tab variable
info_tab = [
    [sg.Text('Title:'), sg.Text('', key='-TITLE-')],
    [sg.Text('Length:'), sg.Text('', key='-LENGTH-')],
    [sg.Text('Views:'), sg.Text('', key='-VIEWS-')],
    [sg.Text('Author:'), sg.Text('', key='-AUTHOR-')],
    [
        sg.Text('Description:'),
        sg.Multiline('', key='-DESCRIPTION-', size=(40, 20),
                    no_scrollbar=True, disabled=True)
    ]
]

# define the content of main_layout second tab as download_tab variable
download_tab = [
    [sg.Frame('Best Quality', [[
        sg.Button('Download', key='-BEST-'),
        sg.Text('', key='-BESTRES-'),
        sg.Text('', key='-BESTSIZE-')]])],
    [sg.Frame('Worst Quality', [[
        sg.Button('Download', key='-WORST-'),
        sg.Text('', key='-WORSTRES-'),
        sg.Text('', key='-WORSTSIZE-')]])],
    [sg.Frame('Audio', [[
        sg.Button('Download', key='-AUDIO-'),
        sg.Text('', key='-AUDIOSIZE-')]])],
    [sg.VPush()],
    [sg.Progress(100, orientation='h', size=(20, 20),
                key='-DOWNLOADPROGRESS-', expand_x=True)]
]

# defining the main_layout that puts together the previously defined first and second tab
main_layout = [
    [sg.TabGroup([
        [sg.Tab('info', info_tab), sg.Tab('Download', download_tab)]
    ])
    ]
]

def main():

    # changes the theme of GUI app
    sg.theme('Darkred2')

    # creates app instance with name and first layout defined as 'start_layout'
    window = sg.Window('YT Converter', start_layout)

    # the actual app loop
    while True:
        # reads the values from user input event
        event, values = window.read()

        # closes the app if cancel or window is closed
        if event == sg.WIN_CLOSED or event == 'Cancel':
            break
        
        # loop continues here if some value has been submitted in the first window
        if event == 'submit':
            # defines the PyTube video_object as per URL given by user for later handling
            video_object = YouTube(values['-INPUT-'], on_progress_callback=progress_check, on_complete_callback=on_complete)
            
            # closes the start_layout window
            window.close()

            # Creates the second app instance, this time with main_layout
            window = sg.Window('Converter', main_layout, finalize=True)
            # udpates all fields with data from video_object
            window['-TITLE-'].update(video_object.title)
            window['-LENGTH-'].update(f'{round(video_object.length / 60,2)} minutes')
            window['-VIEWS-'].update(video_object.views)
            window['-AUTHOR-'].update(video_object.author)
            window['-DESCRIPTION-'].update(video_object.description)

            # updates the buttons defined previously under download_tab to include appropriate data as per stream from video_object
            window['-BESTSIZE-'].update(
                f'{round(video_object.streams.get_highest_resolution().filesize / 1048576,1)} MB')
            window['-BESTRES-'].update(
                video_object.streams.get_highest_resolution().resolution)

            window['-WORSTSIZE-'].update(
                f'{round(video_object.streams.get_lowest_resolution().filesize / 1048576,1)} MB')
            window['-WORSTRES-'].update(
                video_object.streams.get_lowest_resolution().resolution)

            window['-AUDIOSIZE-'].update(
                f'{round(video_object.streams.get_audio_only().filesize / 1048576,1)} MB')

        # starts the download as per selected stream
        if event == '-BEST-':
            video_object.streams.get_highest_resolution().download()

        if event == '-WORST-':
            video_object.streams.get_lowest_resolution().download()

        if event == '-AUDIO-':
            video_object.streams.get_audio_only().download()

    # closes the window if While loop exits
    window.close()

    # end of main function

if __name__ == "__main__":
    main()