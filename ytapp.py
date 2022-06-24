from pytube import YouTube
import pytube.request
from colorama import init, Fore, Back, Style

# Change the value here to something smaller to decrease chunk sizes,
#  thus increasing the number of times that the progress callback occurs
pytube.request.default_range_size = 437184  # 9MB chunk size

init()
#link = str(input("Enter Youtube URL: "))
link = "https://www.youtube.com/watch?v=CML6vfKjQss"

def on_complete(stream, filepath):
    print("Download complete!")        
    print(filepath)
        
def on_progress(stream, chunk, bytes_remaining):
    progress_string = f'{round(100 - (bytes_remaining / stream.filesize * 100),1)}%'
    print("Downloading...")
    print(progress_string)

video_object = YouTube(link, on_complete_callback = on_complete, on_progress_callback = on_progress)

def get_video_info(video_object):
    print('\n<------------------------  Video info  --------------------------------->\n')
    print(Fore.GREEN + Back.CYAN + Style.BRIGHT + f' Title:  {Style.RESET_ALL}{Style.BRIGHT} {video_object.title}')
    print(Fore.GREEN + Back.CYAN + Style.BRIGHT + f' Length: {Style.RESET_ALL}{Style.BRIGHT} {round(video_object.length / 60,2)} minutes')
    print(Fore.GREEN + Back.CYAN + Style.BRIGHT + f' Views:  {Style.RESET_ALL}{Style.BRIGHT} {round(video_object.views / 1000000,3)} million')
    print(Fore.GREEN + Back.CYAN + Style.BRIGHT + f' Channel:{Style.RESET_ALL}{Style.BRIGHT} {video_object.author}')
    print(Fore.GREEN + f'    URL:  {Style.RESET_ALL}{Style.BRIGHT}{link}')
    print('\n<---------------------------------------------------------------------->\n')

get_video_info(video_object)

print(
    Fore.BLUE + Style.BRIGHT + 'Download: ' + 
    Fore.GREEN + Style.BRIGHT + f'(b)est {Style.RESET_ALL}|' + 
    Fore.YELLOW + Style.BRIGHT + f'(w)orst {Style.RESET_ALL}|' +
    Fore.CYAN + Style.BRIGHT + f'(a)udio {Style.RESET_ALL}{Style.BRIGHT}| (e)xit'
    )
download_choice = input('Choice: ')

if download_choice == "b": 
    video_object.streams.get_highest_resolution().download()
if download_choice == 'w':
    video_object.streams.get_lowest_resolution().download()
if download_choice == 'a': 
    video_object.streams.get_audio_only().download()
