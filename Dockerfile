# syntax=docker/dockerfile:1

FROM python:3.8-slim-buster

# Copy requirements
COPY requirements.txt requirements.txt

# Install requirements
RUN pip3 install -r requirements.txt

# Set working directory as application catalog
WORKDIR /application

# Copy all the files located in the current directory and copies them into the image
COPY . .

# Set variable = FLASK_APP as main entypoint to application
ENV FLASK_APP=application/app.py

# Run the application
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
