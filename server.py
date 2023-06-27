from flask import Flask, render_template, request,  send_file, send_from_directory, flash
from PIL import Image
import os

app = Flask(__name__, static_folder='static')

if not os.path.exists('uploads'):
    os.makedirs('uploads')


def encode_message(image_path, message, image_name):
    message = message + '*'
    img = Image.open(image_path)
    img = img.convert('RGB')

    width, height = img.size
    pixels = list(img.getdata())

    if len(message) > len(pixels) * 3:
        return "Message too long for this image!"

    encoded_pixels = []
    message_index = 0

    for pixel in pixels:
        r, g, b = pixel

        if message_index < len(message):
            ascii_val = ord(message[message_index])

            # encode the message bits into the least significant bits of the pixel values
            r = (r & 0xF8) | ((ascii_val >> 5) & 0x07)
            g = (g & 0xF8) | ((ascii_val >> 2) & 0x07)
            b = (b & 0xFC) | ((ascii_val >> 0) & 0x03)

            encoded_pixels.append((r, g, b))
            message_index += 1
        else:
            encoded_pixels.append(pixel)

    encoded_img = Image.new(img.mode, img.size)
    encoded_img.putdata(encoded_pixels)

    new_image_path = f"uploads/{image_name}"
    encoded_img.save(new_image_path)
    os.remove(image_path)
    return "Encoding completed successfully!"


def decode_message(image_path):
    img = Image.open(image_path)
    img = img.convert('RGB')

    pixels = list(img.getdata())

    message = ""
    message_index = 0

    while True:
        pixel = pixels[message_index]
        r, g, b = pixel

        # decode the least significant bits of the pixel values into the message bits
        ascii_val = ((r & 0x07) << 5) | ((g & 0x07) << 2) | ((b & 0x03) << 0)

        if chr(ascii_val) in ['#', '*', '\n']:
            break

        message += chr(ascii_val)
        message_index += 1

    return message

static_folder = os.path.abspath('static')
@app.route('/favicon.ico')
def favicon():
    return send_file(os.path.join(static_folder, 'favicon.ico'), mimetype='image/vnd.microsoft.icon')

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/encode', methods=['GET', 'POST'])
def encode():
    if request.method == 'POST':
        text = request.form['text']
        image = request.files['image']
        new_image_name = request.form['new_image_name']

        if not text or not image or not new_image_name:
            return "Invalid input for encoding!"

        image_path = f"uploads/{image.filename}"
        image.save(image_path)

        result = encode_message(image_path, text, new_image_name)

        if result:
            success_message = "Encoding successful!"
            return render_template('encode/encode.html', success_message=success_message)

    return render_template('encode/encode.html')


@app.route('/decode', methods=['GET', 'POST'])
def decode():
    if request.method == 'POST':
        encoded_image = request.files['encoded_image']

        if not encoded_image:
            return "Invalid input for decoding!"

        image_path = f"uploads/{encoded_image.filename}"
        encoded_image.save(image_path)

        result = decode_message(image_path)

        return render_template('decode/decode.html', message=result)

    return render_template('decode/decode.html')



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
