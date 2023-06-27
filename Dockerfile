# use an official Python runtime as the base image
FROM python:3.10-slim-buster

# set the working directory in the container
WORKDIR /app

# copy the requirements.txt file into the container
COPY requirements.txt .

# install dependencies
RUN apt-get update && apt-get install -y \
    libjpeg-dev \
    zlib1g-dev

# install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# copy the application code into the container
COPY . .

# copy the static folder into the container
COPY static static

# expose the port the Flask app runs on
EXPOSE 8080

# Set the command to run the Flask app
CMD [ "python", "server.py" ]

