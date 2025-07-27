# chats/middleware.py
import time
from django.http import JsonResponse

from datetime import datetime
from django.http import HttpResponseForbidden

class RestrictAccessByTimeMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        current_hour = datetime.now().hour

        # Allow access between 6PM (18) and 9PM (21)
        if current_hour < 18 or current_hour >= 21:
            return HttpResponseForbidden("Access to chat is allowed only between 6PM and 9PM.")

        return self.get_response(request)


class RestrictAccessByTimeMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Only restrict access for URLs related to chats
        if request.path.startswith('/chats/'):
            now = datetime.now().time()
            start_time = time(18, 0)  # 6:00 PM
            end_time = time(21, 0)    # 9:00 PM

            if not (start_time <= now <= end_time):
                return HttpResponseForbidden("Access to chats is only allowed between 6PM and 9PM.")

        return self.get_response(request)

class OffensiveLanguageMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.ip_message_log = {}

    def __call__(self, request):
        if request.method == "POST":
            ip = self.get_client_ip(request)
            now = time.time()

            # Clean old entries
            self.ip_message_log.setdefault(ip, [])
            self.ip_message_log[ip] = [t for t in self.ip_message_log[ip] if now - t < 60]

            if len(self.ip_message_log[ip]) >= 5:
                return JsonResponse({"error": "Rate limit exceeded: Max 5 messages per minute"}, status=429)

            self.ip_message_log[ip].append(now)

        return self.get_response(request)

    def get_client_ip(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip

class RolepermissionMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Only check permissions on authenticated users
        user = getattr(request, 'user', None)

        # If user is not authenticated or does not have required role
        if user and user.is_authenticated:
            role = getattr(user, 'role', '').lower()
            if role not in ['admin', 'moderator']:
                return JsonResponse(
                    {'error': 'Permission denied: You do not have access to this resource'},
                    status=403
                )

        # Allow access
        return self.get_response(request)
