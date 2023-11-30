#!/usr/bin/python3
"""Perform assertions to test decompression functionality"""

import unittest
from app.compression import decompress

class TestDecompression(unittest.TestCase):
    def test_decompress_image(self):
        compressed_image_path = 'compressed_test_image.jpg'  # compressed image path
        output_path = 'decompressed_test_image.jpg'
        decompress.decompress_image(compressed_image_path, output_path)


if __name__ == '__main__':
    unittest.main()
