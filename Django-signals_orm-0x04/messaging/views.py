from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Message

@login_required
def delete_user(request):
    user = request.user
    logout(request)  # Log user out before deleting
    user.delete()
    return redirect('home')  # Replace with your actual redirect URL

@login_required
def threaded_messages_view(request):
    # Fetch parent messages (non-replies)
    messages = Message.objects.filter(receiver=request.user, parent_message__isnull=True)\
        .select_related('sender', 'receiver')\
        .prefetch_related('replies__sender', 'replies__receiver')

    return render(request, 'messaging/threaded_messages.html', {'messages': messages})
