#!/usr/bin/env python
#viewMig.py
import zlib
from PIL import Image

def compress(data):
    return zlib.compress(data.encode())

def decompress(data):
    return zlib.decompress(data).decode()

# Function to save image data to .mig file
def save_mig(filename, header, palette, pixel_data):
    with open(filename, 'w') as f:
        f.write(f"{header[0]} {header[1]}\n")
        f.write("#" + "#".join(palette) + "\n")
        for row in pixel_data:
            f.write(row + '\n')

# Function to load image data from .mig file
def load_mig(filename):
    with open(filename, 'rb') as f:
        data = decompress(f.read())
        lines = str(data).split("\n")

        header = lines[0].split(" ")

        palette = lines[1].strip().split("#")[1:]
        pixel_data = [row.strip() for row in lines[2:]]
    return header, palette, pixel_data

def view_image(name):
    # Load image from file
    header, palette, lines = load_mig(name)

    # Create a new blank image with the dimensions specified in the header
    img = Image.new("RGBA", (int(header[0]), int(header[1])))
    # Convert palette colors to RGBA format
    palette_rgba = []
    for color in palette:
        # Check if the color string has the correct length
        if len(color) == 8:  
            rgba_tuple = tuple(int(color[i:i+2], 16) for i in (2, 4, 6, 0))  # Adjust indices to skip alpha
            palette_rgba.append(rgba_tuple)
        elif len(color) == 6:  # If the alpha component is missing
            rgba_tuple = tuple(int(color[i:i+2], 16) for i in (0, 2, 4)) + (255,)  # Add alpha component (default to 255)
            palette_rgba.append(rgba_tuple)
        else:
            print(f"Invalid color string: {color}")
    for y, row in enumerate(lines[2:]):  # Start from index 2 to skip the header and palette lines
        for x, pixel in enumerate(row):
            color_index = ord(pixel) - ord('A')  # Get the index of color in palette
            if 0 <= color_index < len(palette_rgba):
                img.putpixel((x, y), palette_rgba[color_index])

    # Display the image
    img.show()


# what this does:
# reads the uncompressed mig format code,
# compresses it into a usable, and lighter form
# and saves it
def compress_mig():
    with open("img.mig",'r') as f:
        data = f.read()
        data = compress(data)
        with open("output.mig",'wb') as f:
            f.write(data)
