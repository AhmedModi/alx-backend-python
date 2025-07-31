from django.shortcuts import render
from .models import Message
from django.contrib.auth.decorators import login_required

@login_required
def threaded_messages_view(request):
    # Fetch parent messages (non-replies)
    messages = Message.objects.filter(receiver=request.user, parent_message__isnull=True)\
        .select_related('sender', 'receiver')\
        .prefetch_related('replies__sender', 'replies__receiver')

    return render(request, 'messaging/threaded_messages.html', {'messages': messages})
