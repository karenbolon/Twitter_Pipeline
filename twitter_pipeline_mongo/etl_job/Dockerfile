# Use an official Python runtime as a parent image
FROM python:3.8

# Set the working directory in the container to /my_folder
WORKDIR /app

# Copy the requirements file into the container at /app [requirements is a text file with all the #libraries you want to install]
# Copy the requirements file and everything else in this folder
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --upgrade pip
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Run app.py when the container launches
CMD ["python", "/app/etl.py"]
