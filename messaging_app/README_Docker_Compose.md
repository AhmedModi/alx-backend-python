# Docker Compose Multi-Container Setup

This project uses Docker Compose to run a Django messaging application with a MySQL database.

## Services

### 1. Web Service (Django App)
- **Port**: 8000
- **Build**: Uses the Dockerfile in the current directory
- **Environment Variables**: Loaded from `.env` file
- **Dependencies**: Requires the database service to be running

### 2. Database Service (MySQL)
- **Port**: 3306
- **Image**: MySQL 8.0
- **Environment Variables**: Database credentials from `.env` file
- **Persistence**: Data stored in Docker volume `mysql_data`

## Setup Instructions

### 1. Environment Variables
Create a `.env` file in the root directory with the following variables:

```bash
# Django Settings
DEBUG=1
SECRET_KEY=your-secret-key-here
DJANGO_SETTINGS_MODULE=messaging_app.settings

# MySQL Database Settings
MYSQL_ROOT_PASSWORD=rootpassword
MYSQL_DATABASE=messaging_db
MYSQL_USER=messaging_user
MYSQL_PASSWORD=messaging_password
MYSQL_HOST=db
MYSQL_PORT=3306

# Django Database Settings
DB_ENGINE=mysql
DB_NAME=messaging_db
DB_USER=messaging_user
DB_PASSWORD=messaging_password
DB_HOST=db
DB_PORT=3306
```

### 2. Build and Run
```bash
# Build and start all services
docker-compose up --build

# Run in background
docker-compose up -d --build

# Stop services
docker-compose down

# Stop and remove volumes
docker-compose down -v
```

### 3. Database Operations
```bash
# Run Django migrations
docker-compose exec web python manage.py migrate

# Create superuser
docker-compose exec web python manage.py createsuperuser

# Access MySQL shell
docker-compose exec db mysql -u messaging_user -p messaging_db
```

### 4. View Logs
```bash
# View all logs
docker-compose logs

# View specific service logs
docker-compose logs web
docker-compose logs db

# Follow logs in real-time
docker-compose logs -f
```

## Access Points

- **Django App**: http://localhost:8000
- **MySQL Database**: localhost:3306
- **Admin Interface**: http://localhost:8000/admin/

## Troubleshooting

### Common Issues

1. **Port Already in Use**: Ensure ports 8000 and 3306 are not used by other services
2. **Database Connection**: Wait for MySQL to fully start before Django tries to connect
3. **Permission Issues**: Ensure proper file permissions for the `.env` file

### Reset Everything
```bash
# Stop all services and remove everything
docker-compose down -v --remove-orphans
docker system prune -a
```

## Development vs Production

- **Development**: Uses Django development server and DEBUG=True
- **Production**: Use gunicorn (configured in Dockerfile) and set DEBUG=False

## Security Notes

- Never commit `.env` files to version control
- Use strong passwords in production
- Consider using Docker secrets for sensitive data in production
- The `.env` file is already added to `.gitignore`

