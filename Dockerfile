# Use an official Python runtime as a parent image
FROM python:3.8

# Set the working directory to /app
WORKDIR /app

# Copy the contents of the current directory into the container at /app
COPY . .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Configure AWS CLI access
# RUN aws configure set aws_access_key_id <your-access-key> && \
#     aws configure set aws_secret_access_key <your-secret-key> && \
#     aws configure set region <your-region>

# Reference the ECR repository URI
# FROM your-ecr-repository-uri:latest


# Make port 5000 available to the world outside this container
EXPOSE 5000

# Run app.py when the container launches
CMD ["python", "run.py", "--ride-data-path", "ride-data.csv"]