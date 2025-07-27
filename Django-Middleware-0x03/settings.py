MIDDLEWARE = [
    'chats.middleware.OffensiveLanguageMiddleware',
    'chats.middleware.RolepermissionMiddleware',
    # other middlewares
]

ROOT_URLCONF = 'urls'  # if you have urls.py
INSTALLED_APPS = ['chats']  # if needed

SECRET_KEY = 'your-secret-key'
DEBUG = True
ALLOWED_HOSTS = ['*']
