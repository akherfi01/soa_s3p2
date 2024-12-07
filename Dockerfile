# Use the official Python 3.11.9 image as the base image
FROM python:3.11.9-slim


# Install git and dependencies
RUN apt-get update && apt-get install -y git \
    && rm -rf /var/lib/apt/lists/*  # Clean up to reduce image size

# Set the working directory inside the container
WORKDIR /app

RUN git clone https://github.com/akherfi01/soa_s3p2.git /app/soa_s3p2
# Install pip dependencies (if you have any)
RUN pip install --upgrade pip \
    && pip install spyne zeep requests flask sqlalchemy


# Expose a port if necessary (optional)
EXPOSE 5000

# Set the default command to run the start.sh script
# Start the server in the background and then run the CLI client
CMD ["python", "/app/soa_s3p2/start_script.py"]

