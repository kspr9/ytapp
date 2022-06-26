from ytdl import get_video_object, get_video_info, get_all_video_streams, dl_video

#prompting user for the URL
url = str(input("Give video url: "))

# defining the video object as per users link
video_object = get_video_object(url)
# presenting the video info
get_video_info(video_object)
# getting DL options
get_all_video_streams(video_object)
#DLing the selected stream/video
dl_video(video_object)