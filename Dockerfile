# syntax=docker/dockerfile:1

FROM python:3.8-slim-buster

WORKDIR /app

# Copy requirements
COPY requirements.txt requirements.txt
# Install requirements
RUN pip3 install -r requirements.txt

# takes all the files located in the current directory and copies them into the image
COPY . .

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]