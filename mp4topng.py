import sys
import os
from moviepy.video.io.VideoFileClip import VideoFileClip

# Get the video file name from the command line argument
video_file = sys.argv[1]

# Get the starting time and interval time from the command-line arguments
start_time = float(sys.argv[2]) if len(sys.argv) > 2 else 0
interval_time = float(sys.argv[3]) if len(sys.argv) > 3 else 0

# Create the "frames" directory if it doesn't exist
if not os.path.exists("frames"):
    os.makedirs("frames")

# Open the video file
clip = VideoFileClip(video_file)

# Get the number of frames that have been processed so far
num_frames_processed = 0
if os.path.exists("frames/progress.txt"):
    with open("frames/progress.txt", "r") as f:
        video_file_name = f.readline().strip()
        if video_file_name == video_file:
            num_frames_processed = int(f.readline())
        else:
            os.remove("frames/progress.txt")

# Iterate through frames and save them as images
frames = int(clip.fps * interval_time) if interval_time > 0 else int(clip.fps * clip.duration)
for i in range(num_frames_processed, frames):
    clip.save_frame("frames/frame%d.png" % i, t=start_time + (i / clip.fps))
    print(f"Processing frame {i+1}/{frames}", end="\r")
    with open("frames/progress.txt", "w") as f:
        f.write(f"{video_file}\n{i+1}")

print(f"Frames of {video_file} are extracted successfully!")

# Clean the progress.txt file
os.remove("frames/progress.txt")

