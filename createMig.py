#!/usr/bin/env python
#createMig.py
from PIL import Image
import zlib

def compress(data):
    return zlib.compress(data.encode())

def get_color_palette(img):
    palette = []
    for color in img.getdata():
        if color not in palette:
            palette.append(color)
    return palette

def create_color_palette_dict(palette):
    palette_dict = {}
    for i, color in enumerate(palette):
        palette_dict[color] = chr(65 + i)  # Assign letters A, B, C, ... to colors
    return palette_dict

def convert_image_to_mig(img, palette_dict):
    width, height = img.size
    pixel_data = ""
    for y in range(height):
        for x in range(width):
            color = img.getpixel((x, y))
            pixel_data += palette_dict[color]
        pixel_data += '\n'
    return pixel_data

def save_mig(filename, width, height, palette, pixel_data):
    with open(filename, 'w') as f:
        f.write(f"{width} {height}\n")
        f.write("#" + "#".join([f"{color[0]:02x}{color[1]:02x}{color[2]:02x}" for color in palette]) + "\n")
        f.write(pixel_data)

def png_to_mig(png_filename, mig_filename):
    # Open PNG file
    img = Image.open(png_filename)
    
    # Get color palette
    palette = get_color_palette(img)
    
    # Create color palette dictionary
    palette_dict = create_color_palette_dict(palette)
    
    # Convert image pixels to letters based on color palette
    pixel_data = convert_image_to_mig(img, palette_dict)
    
    # Save .mig file
    save_mig(mig_filename, img.width, img.height, palette, pixel_data)

    with open(mig_filename,'r') as f:
        data = f.read()
        data = compress(data)
        with open(mig_filename,'wb') as f:
            f.write(data)
        print(f"saved compressed mig to {mig_filename}")
