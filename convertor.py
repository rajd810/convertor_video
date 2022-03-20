import os
# os.environ["IMAGEIO_FFMPEG_EXE"] = "/usr/bin/ffmpeg"
from moviepy.editor import *


mp4_file = r'/Users/rajdhumal/Desktop/Python_Project/MP4 to MP3/mp4/sample.mp4'
mp3_file = r'/Users/rajdhumal/Desktop/Python_Project/MP4 to MP3/mp4/sample.mp3'


videoclip = VideoFileClip(mp4_file)
audioclip = videoclip.audio
audioclip.write_audiofile(mp3_file)
audioclip.close()
videoclip.close()
