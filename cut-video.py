# Needs moviepy
# $ pip install moviepy

from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
from datetime import datetime, timedelta
import os

def time_to_seconds(time_str):
    time_format = "%M:%S"
    if ':' in time_str:
        time_data = datetime.strptime(time_str, time_format)
        return time_data.minute * 60 + time_data.second
    else:
        return int(time_str)

def cut_video(file_path, start_time, end_time):
    start_time = time_to_seconds(start_time)
    end_time = time_to_seconds(end_time)

    output_file = "cutted_" + os.path.basename(file_path)
    ffmpeg_extract_subclip(file_path, start_time, end_time, targetname=output_file)

    print(f"Video cutted successfully. Output file is: {output_file}")

# usage
path = r"C:\Users\marti\Desktop\video.mp4"
minute_start = "36:55"
minute_end = "37:05"

cut_video(path, minute_start, minute_end)