# Use the official Python image as the base image
FROM python:3

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
# Get AWS credentials from env
# ENV AWS_ACCESS_KEY_ID=${AWS_ACCESS_KEY_ID}
# ENV AWS_SECRET_ACCESS_KEY=${AWS_SECRET_ACCESS_KEY}
# ENV AWS_SESSION_TOKEN=${AWS_SESSION_TOKEN}
# ENV AWS_DEFAULT_REGION=${AWS_DEFAULT_REGION}

# Create and set the working directory in the container
WORKDIR /app

# Install system dependencies
RUN apt-get update \
    && apt-get install -y python3-dev libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt /app/
RUN pip install --upgrade pip \
    && pip install -r requirements.txt

# Copy the Django project into the container
COPY . /app/

# Collect static files
# RUN python manage.py collectstatic --noinput 

# Start the Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]