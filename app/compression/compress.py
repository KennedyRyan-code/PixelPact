#!/usr/bin/python3

from PIL import Image

def compress_image(image_path, output_path, quality=50):
    img = Image.open(image_path)
    img.save(output_path, quality=quality)
