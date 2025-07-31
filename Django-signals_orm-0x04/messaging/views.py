from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Message

@login_required
def unread_messages_view(request):
    unread_messages = Message.unread.for_user(request.user)
    return render(request, 'messaging/unread_messages.html', {'unread_messages': unread_messages})
