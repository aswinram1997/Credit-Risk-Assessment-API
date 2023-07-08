# Use the official Python 3.8 base image
FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /app

# Copy the code into the container
COPY ./ /app

# Install the dependencies
RUN pip install --no-cache-dir -r /app/requirements.txt

# Expose the port used by FastAPI
EXPOSE 8000

# Start the FastAPI application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
