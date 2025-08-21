# Use Python 3.10 as base image
FROM python:3.10-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set work directory
WORKDIR /app

# Install system dependencies
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        gcc \
        default-libmysqlclient-dev \
        pkg-config \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . /app/

# Collect static files (safe even if not needed)
RUN python manage.py collectstatic --noinput || true

# Expose port
EXPOSE 8000

# Start Django app with Gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "messaging_app.wsgi:application"]
