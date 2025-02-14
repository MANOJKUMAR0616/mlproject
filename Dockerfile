FROM python:3.11.7-slim-buster

WORKDIR /app

# Copy all files from the current directory to /app in the container
COPY . /app

# Install dependencies
RUN pip install -r requirements.txt

# Run the application
CMD ["python3", "app.py"]

