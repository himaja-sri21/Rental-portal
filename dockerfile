# Use official Python image
FROM python:3.11

# Set working directory
WORKDIR /app

# Copy requirements first (better caching)
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

# Expose port (change if your app uses different one)
EXPOSE 5000

# Run the app
CMD ["python", "app.py"]