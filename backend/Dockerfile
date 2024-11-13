# Use the official Python base image
FROM python:3.9

# Sets the working directory inside the container
WORKDIR /app

# Copy the necessary files to the container
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the wait-for-it.sh file to the container
COPY wait-for-it.sh /app/wait-for-it.sh

# Give execution permissions to the script
RUN chmod +x /app/wait-for-it.sh

# Copy the rest of the code to the container
COPY . .

# Expose port 8000 for FastAPI
EXPOSE 8000

# Run the FastAPI server when the container starts
CMD ./wait-for-it.sh db:5432 -- uvicorn main:app --host 0.0.0.0 --port 8000 --reload
