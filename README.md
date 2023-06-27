#### Copyright 2023-2024 Stoica Mihai-Bogdan 315CA (bogdanstoicasn@yahoo.com)
#### GNU GENERAL PUBLIC LICENSE 
#### Version 3, 29 June 2007


# Web-based stenography tool


## Decode/Encode script

In the archive, the file "image_manip.py" is just the script that
encodes/decodes an image. To run it we use the command:

> python image_manip.py encode "image_path" "message" "output_name"
(for encoding)

> python image_manip.py decode "output_name" (for decoding)


## The web-based app

**Encoding Process:**

1. On the main page, click the "Encode" button.

2. Fill in the required fields.

3. Click "Encode".

4. If the encoding process is successful, you will see a message indicating
that the encoding was completed.

5. The newly encoded image will be saved in the "uploads" directory with the
provided image name.

**Decoding Process:**

1. On the main page, click the "Decode" button.

2. Choose image

3. Click "Decode" button.

4. The decoded message will be displayed on the page.

**File Structure:**

>server.py: The main Flask application file containing the route handlers and the encoding/decoding functions.

> index.html: The HTML template for the main page.

> encode/encode.html: The HTML template for the encode page.

> decode/decode.html: The HTML template for the decode page.

> static/: The directory containing static files (favicon).

> uploads/: The directory where uploaded and encoded images are stored.

**Challenges:**

> understanding Flask: Flask is a micro web framework that requires some
knowledge of web development concepts such as routing, templates, and
request handling.

> handling File Uploads: The program allows users to upload image files for
encoding and decoding. Handling file uploads can be tricky, especially when
it comes to validating file types, managing file storage.

> image Encoding/Decoding: The core functionality of this program involves
encoding text into images and decoding text from encoded images. This process
requires an understanding of image manipulation techniques.To ensure that the
process is working, I put * as the last character of the encoded message, so
that the decoding goes until we find *.


## Docker and requirements

The **requirements.txt** file lists the Python dependencies required by the
Flask application.

The **Dockerfile** is used to build a Docker image that encapsulates the Flask
application and it's dependencies.

> build -> docker build -t iap-tema2 .

> run -> docker run -p 8080:8080 iap-tema2

**Usage:**

1. Build the Docker image using the Dockerfile.

2. Run the Docker image as a container.

3. Access the application by navigating to http://localhost:8080 in your web
browser.

4. Use the web interface to encode and decode messages into images.
 
 
## Resources

-> [PIL](https://pillow.readthedocs.io/en/stable/)

-> [Flask](https://flask.palletsprojects.com/en/2.3.x/)

-> [Stegano](https://www.kaspersky.com/resource-center/definitions/what-is-steganography) 
