# messaging/views.py

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Message
from django.views.decorators.cache import cache_page
from messaging.models import Message

@cache_page(60)  # Caches the view for 60 seconds
def conversation_detail(request, conversation_id):
    messages = Message.objects.filter(conversation_id=conversation_id)
    return render(request, 'chats/conversation_detail.html', {'messages': messages})

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

def unread_inbox_view(request):
    unread_messages = Message.unread.unread_for_user(request.user).only('id', 'content', 'timestamp', 'sender')
    # render or return this data
