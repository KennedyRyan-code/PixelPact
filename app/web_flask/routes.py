#!/usr/bin/python3

from flask import Flask, request, send_file
from app.compression import compress, decompress

app = Flask(__name__)

@app.route('/api/compress', methods=['POST'])
def compress_image():
    if 'file' not in request.files:
        return 'No file part'

    file = request.files['file']
    output_path = '/app/images/compressed_imgs/comp_image.jpg'  # output path
    compress.compress_image(file, output_path)
    return send_file(output_path, as_attachment=True)

@app.route('/api/decompress', methods=['POST'])
def decompress_image():
    if 'file' not in request.files:
        return 'No file part'

    file = request.files['file']
    output_path = '/app/images/decompressed_imgs/decomp_image.jpg'  #  output path
    decompress.decompress_image(file, output_path)
    return send_file(output_path, as_attachment=True)

@app.route('/')
def index():
    return app.send_static_file('/static/index.html')
