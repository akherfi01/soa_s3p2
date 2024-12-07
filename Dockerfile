# Use the official Python 3.11.9 image as the base image
FROM python:3.11.9-slim

# Set the working directory inside the container
WORKDIR /app

# Install pip dependencies (if you have any)
RUN pip install --upgrade pip \
    && pip install spyne zeep requests flask sqlalchemy


# Copy the local repository to the container
COPY ./project /app/project
# Expose a port if necessary (optional)
EXPOSE 5000

# Set the default command to run the start.sh script
CMD python /app/project/app.py && python /app/project/tests/soa_project_interface_ask.py

