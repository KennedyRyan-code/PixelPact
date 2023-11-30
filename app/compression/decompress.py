#!/usr/bin/python3

from PIL import Image

def decompress_image(compressed_image_path, output_path):
    compressed_img = Image.open(compressed_image_path)
    compressed_img.save(output_path)
