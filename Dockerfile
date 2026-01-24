# Use Python 3.15 Alpine as the base image
FROM python:3.15-rc-alpine3.23

# Set working directory inside the container
WORKDIR /app

# Copy requirements.txt if you have dependencies
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your application code
COPY . .

# Expose a port if your app runs on a specific port (example 5000 for Flask)
EXPOSE 5000

# Command to run the application
# Replace app.py with your main python file
CMD ["python3", "app.py"]
