# Use an official Python runtime as a parent image
FROM python:3.11

# Set the working directory to /app
WORKDIR /app

# Install dependencies
COPY requirements.txt /app/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy the current directory contents into the container at /app
COPY . /app/

# Collect static files
# RUN python manage.py collectstatic --noinput

# Expose port 8000 to allow external connections
EXPOSE 8000

# Define the command to run on container start
# CMD ["gunicorn", "--bind", "0.0.0.0:8000", "shikshakikiran.wsgi:application"]
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
