# Use a slim version of Python
FROM python:3.11-slim

# Set work directory in container
WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the project files
COPY . .

# Optional: expose port if you're using Flask or FastAPI
EXPOSE 5000

# Default command to run your app
CMD ["python", "app.py"]

