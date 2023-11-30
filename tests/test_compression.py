#!/usr/bin/python3
"""Perform assertions to test compression functionality"""

import unittest
from app.compression import compress

class TestCompression(unittest.TestCase):
    def test_compress_image(self):
        image_path = 'test_image.jpg'  # a test image path
        output_path = 'compressed_test_image.jpg'
        compress.compress_image(image_path, output_path)


if __name__ == '__main__':
    unittest.main()
