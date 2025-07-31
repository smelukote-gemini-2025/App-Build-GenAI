    # Use an official Python runtime as a parent image
    FROM python:3.9-slim

    # Set the working directory in the container
    WORKDIR /app

    # Copy the current directory contents into the container at /app
    COPY . /app

    # Install any needed dependencies specified in requirements.txt
    RUN pip install --no-cache-dir -r requirements.txt

    # Expose the port the app runs on
    EXPOSE 8080

    # Run the Gunicorn server
    CMD ["gunicorn", "--bind", "0.0.0.0:8080", "app:app"]