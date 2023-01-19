import os
import sys
from PIL import Image

# Set the number of pixels to crop
top_crop = 55
bottom_crop = 55

# Get the folder path passed as an argument when running the program
try:
    folder = sys.argv[1]
except IndexError:
    print("Please provide a folder path as an argument when running the program.")
    sys.exit()

# Check if the folder path is valid
if not os.path.isdir(folder):
    print("Invalid folder path.")
    sys.exit()

# Loop through all PNG files in the specified folder
for filename in os.listdir(folder):
    if filename.endswith(".png"):
        # Open the image
        im = Image.open(os.path.join(folder, filename))

        # Get the width and height of the image
        width, height = im.size

        # Crop the image
        im = im.crop((0, top_crop, width, height-bottom_crop))

        # Save the cropped image with the same name as the input file
        im.save(os.path.join(folder, filename))

