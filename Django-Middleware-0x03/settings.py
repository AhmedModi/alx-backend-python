MIDDLEWARE = [
    # Default Django middleware
    'django.middleware.security.SecurityMiddleware',
    
    # ✅ Add your custom middleware
    'chats.middleware.RequestLoggingMiddleware',

    # ✅ Custom middleware
    'chats.middleware.RequestLoggingMiddleware',
    'chats.middleware.RestrictAccessByTimeMiddleware',

    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
