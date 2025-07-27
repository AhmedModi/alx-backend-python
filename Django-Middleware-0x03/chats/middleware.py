# chats/middleware.py

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
