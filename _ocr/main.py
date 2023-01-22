import requests

from flask import Flask,render_template, request
from werkzeug.utils import secure_filename

app = Flask(__name__)


def receipt_processing(test_file):

    test_file.save(test_file.filename)

    f = open(test_file, "r")

    out = open("out.txt", "w")

    return f

    for line in f:
        space_idx = line.find(" ")
        out.write(line[space_idx+1:])
        decimal_idx = line.find(".")
        out.write(line[decimal_idx-3:decimal_idx+2])

import cloudmersive_ocr_api_client
from cloudmersive_ocr_api_client.rest import ApiException

api_instance = cloudmersive_ocr_api_client.ImageOcrApi()
image_file = 'receipt.jpg' # file | Image file to perform OCR on.  Common file formats such as PNG, JPEG are supported.

api_instance.api_client.configuration.api_key = {}
api_instance.api_client.configuration.api_key['Apikey'] = 'b0a5e6da-ae28-44c8-a4d7-9768d6c9195f'

try:
    # Converts an uploaded image in common formats such as JPEG, PNG into text via Optical Character Recognition.
    api_response = api_instance.image_ocr_post(image_file)
    print(api_response)
except ApiException as e:
    print("Exception when calling ImageOcrApi->image_ocr_post: %s\n" % e)

if __name__ == '__main__':
    app.run(debug=True)


