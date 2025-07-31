from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Message

@login_required
def sent_messages_view(request):
    messages = Message.objects.filter(sender=request.user)\
        .select_related('receiver')\
        .prefetch_related('replies')

    return render(request, 'messaging/sent_messages.html', {'messages': messages})
