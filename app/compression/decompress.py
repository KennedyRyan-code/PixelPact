#!/usr/bin/python3

from PIL import Image


def decompress_image(compressed_image_path, output_path):
    try:
        compressed_img = Image.open(compressed_image_path)
        compressed_img.save(output_path)
        return True, "Image decompressed successfully"
    except Exception as e:
        return False, f"Error: {e}"
