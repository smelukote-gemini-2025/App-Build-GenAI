# Use an official Python runtime as a parent image
FROM python:3.9-slim-buster

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the working directory
COPY requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your application code into the working directory
COPY . .

# Cloud Run services listen on the port specified by the PORT environment variable.
# Define the port your app will listen on.
ENV PORT 8080

# Run the web service on container startup.
# Cloud Run will automatically pass the PORT env var to your container.
CMD ["python", "main.py"]
