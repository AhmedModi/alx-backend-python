# Docker Setup for Messaging App

This document explains how to containerize and run the Building Robust APIs messaging application using Docker.

## Prerequisites

- Docker installed on your system
- Git repository cloned

## Files Created

1. **requirements.txt** - Contains all Python dependencies
2. **Dockerfile** - Instructions for building the Docker image
3. **.dockerignore** - Excludes unnecessary files from Docker build
4. **docker-compose.yml** - Simplifies running the container

## Quick Start with Docker

1. **Build the Docker image:**
   ```bash
   docker build -t messaging-app .
   ```

2. **Run the container:**
   ```bash
   docker run -d -p 8000:8000 --name messaging-app-container messaging-app
   ```

3. **Access the application:**
   - Main app: http://localhost:8000
   - Admin interface: http://localhost:8000/admin/
   - API endpoints: http://localhost:8000/api/chats/
   - Conversations: http://localhost:8000/api/chats/conversations/

4. **Stop and remove the container:**
   ```bash
   docker stop messaging-app-container
   docker rm messaging-app-container
   ```

## Quick Start with Docker Compose

1. **Build and run the application:**
   ```bash
   docker-compose up --build
   ```

2. **Access the application:**
   - Main app: http://localhost:8000
   - Admin interface: http://localhost:8000/admin/
   - API endpoints: http://localhost:8000/api/

3. **Stop the application:**
   ```bash
   docker-compose down
   ```

## Manual Docker Commands

### Build the Docker Image

```bash
# Navigate to the messaging_app directory
cd messaging_app

# Build the Docker image
docker build -t messaging-app .
```

### Run the Container

```bash
# Run the container
docker run -p 8000:8000 messaging-app
```

### Run with Volume Mounting (for development)

```bash
# Run with current directory mounted for live code changes
docker run -p 8000:8000 -v $(pwd):/app messaging-app
```

## Dockerfile Details

The Dockerfile:
- Uses Python 3.10 slim image
- Installs system dependencies
- Installs Python packages from requirements.txt
- Copies application code
- Exposes port 8000
- Uses Gunicorn as the WSGI server

## Environment Variables

- `DEBUG=1` - Enables Django debug mode
- `DJANGO_SETTINGS_MODULE=messaging_app.settings` - Specifies Django settings

## Troubleshooting

### Port Already in Use
If port 8000 is already in use, change the port mapping:
```bash
docker run -p 8001:8000 messaging-app
```

### Permission Issues
On Linux/macOS, you might need to use sudo:
```bash
sudo docker build -t messaging-app .
```

### Database Issues
The app uses SQLite by default. For production, consider using PostgreSQL or MySQL.

## Production Considerations

- Set `DEBUG=0` in production
- Use environment variables for sensitive data
- Consider using a reverse proxy (nginx)
- Use proper database configuration
- Implement proper logging and monitoring
