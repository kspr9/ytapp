from pytube import YouTube


def get_video_info(url):
    video_object = YouTube(url)
    print(f'title:  {video_object.title}')
    print(f'length: {round(video_object.length / 60,2)} minutes')
    print(f'views:  {round(video_object.views / 1000000,3)} million')
    print(f'author: {video_object.author}')

def get_video_object(url, stream):
        
    def on_complete(stream, filepath):
        print("Download complete!")
        print(filepath)

    def on_progress(stream, chunk, bytes_remaining):
        progress_string = f'100 - {round(bytes_remaining / stream.filesize * 100,2)}%'
        print(progress_string)
    
    return(video_object = YouTube(url, on_complete_callback = on_complete, on_progress_callback = on_progress))

def dl_video(url):
    
    print("\n<-------------------  Video Title  ---------------------->\n")
    #get Video Title
    print(video_object.title)

    print("\n<--------------  Display available streams  -------------->")
    print("""\nThese streams are video and audio in one. 
            For video only or audio only, modify stream filter in sourcecode\n""")
   
    ###>>> get all the streams with video+audio 
    for stream in video_object.streams.filter(progressive=True):
        print(stream)

    print("\n<--------------  Display audio-only streams  -------------->")
    print("""\nThese streams are audio only ie only_audio=True.\n""")

    ###>>> get all the streams with video+audio
    for stream in video_object.streams.filter(only_audio=True):
        print(stream)

    print("\n<---------------  Stream selection  ---------------------->\n")
    # select preferred stream
    chosen_stream = int(input("Which itag do you choose?: "))

    selected_stream = video_object.streams.get_by_itag(chosen_stream)

    print("\n<---------------  Download started  ---------------------->\nDownloading...")

    stream.download()
    print("\n<----------------  Download finished  -------------------->\n")

if __name__ == "__main__":
    
    url = str(input("Give video url: "))
    get_video_info(url)
    dl_video(url)