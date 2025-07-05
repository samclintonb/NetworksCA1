# Use official Python 3.9 base image
FROM python:3.9

# Set working directory inside container
WORKDIR /app

# Copy app.py, templates, and static folders into container
COPY app.py /app/
COPY templates /app/templates
COPY static /app/static

# Install Flask
RUN pip install flask

# Expose port 80 to map container port to host
EXPOSE 80

# Run the Flask app on 0.0.0.0:80
CMD ["python3", "app.py"]
