from pytube import YouTube
from ytdl import dl_video, get_video_info

link = str(input("Enter Youtube URL: "))

# info about video
get_video_info(link)

# Downloading
dl_video(link)

# so here is basically the same logic that I had under the main function of the ytdl.py program

'''
print('Download: (b)est | (w)orst | (a)udio | (e)xit')
download_choice = input('Choice: ')

match download_choice:
    case 'b':
        video_object.streams.get_highest_resolution().download(r'/home/kaspar/Downloads')
    case 'w':
        video_object.streams.get_worst_resolution().download(r'/home/kaspar/Downloads')
    case 'a':
        video_object.streams.get_audio_only().download(r'/home/kaspar/Downloads')
'''
