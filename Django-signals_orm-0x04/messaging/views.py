# messaging/views.py

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Message

@login_required
def unread_messages_view(request):
    # ✅ Use the custom manager + .only() + .select_related()
    unread_messages = Message.unread.unread_for_user(request.user).select_related('sender', 'receiver')
    return render(request, 'messaging/unread_messages.html', {'unread_messages': unread_messages})
