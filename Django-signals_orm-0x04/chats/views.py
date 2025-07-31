from django.shortcuts import render
from django.views.decorators.cache import cache_page
from messaging.models import Message

@cache_page(60)  # Caches the view for 60 seconds
def conversation_detail(request, conversation_id):
    messages = Message.objects.filter(conversation_id=conversation_id)
    return render(request, 'chats/conversation_detail.html', {'messages': messages})
