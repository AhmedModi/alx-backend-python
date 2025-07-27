MIDDLEWARE = [
    # Default Django middleware
    'django.middleware.security.SecurityMiddleware',
    
    # ✅ Add your custom middleware
    'chats.middleware.RequestLoggingMiddleware',

    # Rest of Django middleware
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
