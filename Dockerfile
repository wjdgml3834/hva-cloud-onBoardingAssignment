# Use an official Python 3.9 image as a parent image
FROM python:3.9-slim

# Set the working directory in the docker image
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 5000 available to the world outside this container
EXPOSE 5001

# Run app.py when the container launches
CMD ["flask", "run", "--host=0.0.0.0"]
