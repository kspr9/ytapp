# a Python script to download any Youtube video

from pytube import YouTube
from pytube.cli import on_progress
import pytube.request

# Change the value here to something smaller to decrease chunk sizes,
#  thus increasing the number of times that the progress callback occurs
pytube.request.default_range_size = 537184  # 9MB chunk size


def get_video_object(url):
    # used for progress bar
    def on_complete(stream, filepath):
        print("Download complete!")
        print(filepath)
    # used for progress bar
    #def on_progress(stream, chunk, bytes_remaining):
    #    progress_string = f'{round(100 - (bytes_remaining / stream.filesize * 100),2)}%'
    #    print(f'{progress_string}\r')
    
    ##  https://stackoverflow.com/questions/44565704/how-to-clear-only-last-one-line-in-python-output-console
    ##  https://stackoverflow.com/questions/63521418/how-to-fix-a-progress-bar-at-the-terminals-last-line-using-python


    #saving video object into a variable
    video_object = YouTube(url, on_complete_callback = on_complete, on_progress_callback = on_progress)

    return(video_object)

def get_all_video_streams(video_object):
    print("\n<------------------  Display audio+video streams  ------------------->")
    ###>>> get all the streams with video+audio 
    for stream in video_object.streams.filter(progressive=True):
        print(stream)
    
    print("\n<-------------------  Display audio-only streams  ------------------->")
    print("""\nThese streams are audio only ie only_audio=True.\n""")

    ###>>> get all the streams with video+audio
    for stream in video_object.streams.filter(only_audio=True):
        print(stream)
    


def get_video_info(video_object):
    print('\n<------------------------  Video info  --------------------------------->\n')
    print(f'title:  {video_object.title}')
    print(f'length: {round(video_object.length / 60,2)} minutes')
    print(f'views:  {round(video_object.views / 1000000,3)} million')
    print(f'author: {video_object.author}')
    print('\n<---------------------------------------------------------------------->')


def dl_video(video_object):
    print("\n<---------------  Stream selection  ---------------------->\n")
    # select preferred stream
    chosen_stream = int(input("Which itag do you choose?: "))

    selected_stream = video_object.streams.get_by_itag(chosen_stream)

    print("\n<---------------  Download started  ---------------------->\nDownloading...")

    selected_stream.download()
    print("\n<----------------  Download finished  -------------------->\n")

if __name__ == "__main__":
    url = str(input("Give video url: "))
    video_object = get_video_object(url)
    get_video_info(video_object)
    get_all_video_streams(video_object)
    dl_video(video_object)