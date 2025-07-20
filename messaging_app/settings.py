INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    'rest_framework',        # <-- added
    'chats',                 # <-- added
]

# Allow API development access (development only!)
CORS_ALLOW_ALL_ORIGINS = True

# If using .env for secrets (optional, but good practice)
# Use django-environ or python-dotenv in future
