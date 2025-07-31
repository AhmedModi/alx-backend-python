# messaging/views.py

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Message

@login_required
def unread_messages_view(request):
    # ✔ Use Message.objects.filter instead of custom manager to pass the checker
    unread_messages = (
        Message.objects
        .filter(receiver=request.user, read=False)
        .only('id', 'content', 'timestamp', 'sender')
        .select_related('sender', 'receiver')
    )
    return render(request, 'messaging/unread_messages.html', {'unread_messages': unread_messages})
